import datetime
import jwt
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework.response import Response

from core.models import User
from core.serializers import UserSerializer


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth = get_authorization_header(request).split()
        if auth:
            token = auth[1]
            user_id = decode_access_token(token)
            if user_id == 'Signature expired. Please log in again.':
                raise exceptions.AuthenticationFailed("Signature expired. Please log in again.")
            user = User.objects.filter(id=user_id).first()
            return user, None

        raise exceptions.AuthenticationFailed("Authentication credentials were not provided.")


def create_access_token(id):
    return jwt.encode({
        'user_id': id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=30),
        'iat': datetime.datetime.utcnow()
    }, 'access_secret', algorithm='HS256')


def decode_access_token(token):
    try:
        payload = jwt.decode(token, 'access_secret', algorithms=['HS256'])
        return payload['user_id']
    except:
        return 'Signature expired. Please log in again.'


def create_refresh_token(id):
    return jwt.encode({
        'user_id': id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
        'iat': datetime.datetime.utcnow()
    }, 'refresh_secret', algorithm='HS256')


def decode_refresh_token(token):
    try:
        payload = jwt.decode(token, 'refresh_secret', algorithms=['HS256'])
        return payload['user_id']
    except:
        return 'Signature expired. Please log in again.'
