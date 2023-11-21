from django.db import models
from users.models import NULLABLE
from django.conf import settings
from django.utils import timezone


class Habit(models.Model):
    """Habit model"""

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, verbose_name='Пользователь')

    place = models.CharField(max_length=100, verbose_name='Место',  **NULLABLE)
    start = models.DateTimeField(verbose_name='Время и дата начала', default=timezone.now)
    action = models.CharField(max_length=250, verbose_name='Действие',  **NULLABLE)
    is_pleasant = models.BooleanField(default=False, verbose_name='Привычка приятная?')
    related_habit = models.ForeignKey('Habit', on_delete=models.SET_NULL, **NULLABLE)
    frequency = models.SmallIntegerField(default=7, verbose_name='Периодичность выполнения')
    reward = models.CharField(max_length=250, verbose_name='Вознаграждение', **NULLABLE)
    time_to_complete = models.DurationField(verbose_name='Время выполнения')
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')

    next_reminder_date = models.DateField(**NULLABLE, verbose_name='Дата следующего напоминания')

    def __str__(self):
        return f'Я буду {self.action} в {self.start} в {self.place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
        ordering = ('start',)
