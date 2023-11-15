from rest_framework import serializers

from habits.models import Habit
from habits.validators import (RelatedHabitOrRewardValidator, TimeToCompleteLimitationValidator,
                               RelatedHabitValidation, PleasantHabitValidation, FrequencyValidation)


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = ('id', 'user', 'place', 'time', 'action', 'is_nice', 'related_habit', 'period', 'reward',
                  'time_to_complete', 'is_public', 'next_reminder_date')
        read_only_fields = ('user',)
        validators = [
            RelatedHabitOrRewardValidator('related_habit', 'reward'),
            TimeToCompleteLimitationValidator('time_to_complete'),
            RelatedHabitValidation('related_habit'),
            PleasantHabitValidation('related_habit', 'is_pleasant', 'reward'),
            FrequencyValidation('frequency')
        ]