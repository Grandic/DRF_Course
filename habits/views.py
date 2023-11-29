from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from habits.models import Habit
from habits.pagination import HabitsPagination
from habits.permissions import IsOwnerOrIsSuperuser
from habits.serializers import HabitSerializer
from habits.services import create_habit_schedule


class HabitCreateAPIView(generics.CreateAPIView):
    """Create new habit and task"""

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        habit = serializer.save()
        create_habit_schedule(habit)


class HabitListAPIView(generics.ListAPIView):
    """Habits list"""

    serializer_class = HabitSerializer
    pagination_class = HabitsPagination
    permission_classes = [IsAuthenticated, IsOwnerOrIsSuperuser]


class PublicHabitsListAPIView(generics.ListAPIView):
    """Is_publict list"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
    pagination_class = HabitsPagination

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Habit.objects.all()
        else:
            return Habit.objects.filter(is_public=True)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Habit info"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrIsSuperuser]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Habit update"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrIsSuperuser]


class HabitDestroyAPIView(generics.DestroyAPIView):
    """Habit delete"""
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrIsSuperuser]
