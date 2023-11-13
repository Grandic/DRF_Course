from django.db import models
from users.models import NULLABLE
from django.conf import settings


class Habit(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, **NULLABLE)
    place = models.CharField(max_length=100, verbose_name='место',  **NULLABLE)
    time = models.DateTimeField(verbose_name='время выполения привычки', **NULLABLE)
    action = models.CharField(max_length=250, verbose_name='действие',  **NULLABLE)
    is_nice = models.BooleanField(default=False, verbose_name='Привычка приятная?')
    reward = models.CharField(max_length=250, verbose_name='действие',  **NULLABLE)


    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)