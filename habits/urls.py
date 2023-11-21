from django.urls import path
from habits.apps import HabitsConfig
from habits.views import (HabitCreateAPIView, HabitListAPIView,
                          PublicHabitsListAPIView, HabitRetrieveAPIView,
                          HabitUpdateAPIView, HabitDestroyAPIView)

app_name = HabitsConfig.name

urlpatterns = [
    path('habits/create/', HabitCreateAPIView.as_view(), name='habit-create'),
    path('habits/', HabitListAPIView.as_view(), name='habit-list'),
    path('habits/public/', PublicHabitsListAPIView.as_view(), name='public_habit-list'),
    path('habits/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit-detail'),
    path('habits/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit-update'),
    path('habits/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit-delete'),
]
