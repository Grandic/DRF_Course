from rest_framework import serializers
from users.models import User


class Userserializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = '__all__'
        # permission_classes = [IsAuthenticated, IsSuperUser]

class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
      #permission_classes = [IsAuthenticated, IsSuperUser | IsModerator | IsOwner]

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # permission_classes = [IsAuthenticated, IsSuperUser]

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # permission_classes = [IsAuthenticated, IsSuperUser]

class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # permission_classes = [IsAuthenticated, IsSuperUser | IsModerator | IsOwner]

