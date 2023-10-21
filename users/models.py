from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True, verbose_name='Email')

    phone = models.CharField(max_length=30, verbose_name='phone number', **NULLABLE)
    country = models.CharField(max_length=30, verbose_name='country', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='avatar', **NULLABLE)
    last_login = models.DateField(verbose_name='Last authentication', default='2023-01-01')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
