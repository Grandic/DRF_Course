from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'date_joined', 'last_login', 'is_active', 'avatar']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
