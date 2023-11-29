from celery import shared_task
from habits.models import Habit
from telebot import TeleBot
from django.conf import settings


@shared_task
def send_telegram_message(habit_id):
    """Send message"""
    habit = Habit.objects.get(id=habit_id)
    bot = TeleBot(settings.TELEGRAM_BOT_API_KEY)
    message = f'Напоминание о выполнении привычки {habit.action} в {habit.start} в {habit.place}'
    bot.send_message(habit.user.chat_id, message)
