from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import CustomUserManager

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """User model"""

    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    phone = models.CharField(unique=True, max_length=35,
                             verbose_name='номер телефона', **NULLABLE)
    avatar = models.ImageField(upload_to='users/',
                               verbose_name='аватар', **NULLABLE)

    # Telegram
    chat_id = models.PositiveIntegerField(verbose_name='chat_id', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
