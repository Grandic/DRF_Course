from django_celery_beat.models import CrontabSchedule, PeriodicTask


def create_habit_schedule(habit):
    """Создание периодичности и задачи на отправку"""
    crontab_schedule, _ = CrontabSchedule.objects.get_or_create(
            minute=habit.start.minute,
            hour=habit.start.hour,
            day_of_month=f'*/{habit.frequency}',
            month_of_year='*',
            day_of_week='*',
            timezone='Europe/Moscow'
        )

    PeriodicTask.objects.create(
        crontab=crontab_schedule,
        name=f'Habit Task - {habit.place}',
        task='habits.tasks.send_telegram_message',
        args=[habit.id],
    )