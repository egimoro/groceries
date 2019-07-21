from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.email
