import datetime
import string
import random

from django.core.mail import send_mail
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import exceptions

from .authentication import create_access_token, create_refresh_token, JWTAuthentication, decode_refresh_token
from .models import User, UserToken, Reset
from .serializers import UserSerializer


class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data
        if data['password'] != data['confirm_password']:
            raise exceptions.APIException("Passwords do not match!")
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginAPIView(APIView):
    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        if email is None or password is None:
            raise exceptions.APIException("Email and password are required!")

        user = User.objects.filter(email=email).first()

        if user is None:
            raise exceptions.APIException("User not found!")

        if not user.check_password(password):
            raise exceptions.APIException("Incorrect password!")

        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)

        UserToken.objects.create(
            user_id=user.id,
            token=refresh_token,
            expired_at=datetime.datetime.utcnow() + datetime.timedelta(days=7),
        )
        response = Response()
        response.set_cookie(key="refresh_token", value=refresh_token, httponly=True)
        response.data = {
            "token": access_token
        }

        return response


class UserAPIView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class RefreshAPIView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        id = decode_refresh_token(refresh_token)

        if not UserToken.objects.filter(
                user_id=id,
                token=refresh_token,
                expired_at__gt=datetime.datetime.utcnow()
        ).exists():
            raise exceptions.AuthenticationFailed("User not found!")

        if id == 'Signature expired. Please log in again.':
            raise exceptions.AuthenticationFailed(id)
        access_token = create_access_token(id)
        return Response({
            "token": access_token
        })


class LogoutAPIView(APIView):

    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        UserToken.objects.filter(token=refresh_token).delete()
        response = Response()
        response.delete_cookie(key='refresh_token')
        response.data = {
            "message": "success"
        }
        return response


class ForgotAPIView(APIView):
    def post(self, request):
        token = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))

        email = request.data.get('email', None)
        Reset.objects.create(
            email=email,
            token=token,
        )
        url = 'http://localhost:3000/reset/' + token
        send_mail(
            subject='Reset Password',
            message='click {url} to reset your password '.format(url=url),
            from_email="angeldahal@email.com",
            recipient_list=[email],
        )

        return Response({
            "message": "success"
        })


class ResetAPIView(APIView):
    def post(self, request):
        data = request.data
        if data['password'] != data['confirm_password']:
            raise exceptions.APIException("Passwords do not match!")
        token = data['token']
        reset = Reset.objects.filter(token=token).first()
        if reset is None:
            raise exceptions.APIException("Invalid token!")
        user = User.objects.filter(email=reset.email).first()
        if not user:
            raise exceptions.APIException("User not found!")
        user.set_password(data['password'])
        user.save()
        return Response({
            "message": "success"
        })