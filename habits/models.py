import datetime

from django.db import models
from users.models import NULLABLE
from django.conf import settings


class Habit(models.Model):
    Period = (
        ('DAILY', 'каждый день'),
        ('WEEKLY', 'раз в неделю'),
    )

    user = models.ForeignKey('users.User', on_delete=models.CASCADE, **NULLABLE)
    place = models.CharField(max_length=100, verbose_name='место',  **NULLABLE)
    time = models.TimeField(verbose_name='время выполения привычки', **NULLABLE)
    action = models.CharField(max_length=250, verbose_name='действие',  **NULLABLE)
    is_nice = models.BooleanField(default=False, verbose_name='Привычка приятная?')


    period = models.CharField(max_length=12, verbose_name='Периодичность выполнения', choices=Period, default='DAILY')
    reward = models.CharField(max_length=250, verbose_name='вознаграждение', **NULLABLE)
    time_to_complete = models.TimeField(verbose_name='Время на выполнение', default=datetime.time(minute=2))
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)



    def __str__(self):
        return f'{self.user} {self.is_nice}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
        ordering = ('is_public',)