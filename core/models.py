from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True, max_length=254)
    password = models.CharField(max_length=255)

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
