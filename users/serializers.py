from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['date_joined', 'last_login', 'avatar', 'groups', 'user_permissions', 'is_superuser', 'is_staff',]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user