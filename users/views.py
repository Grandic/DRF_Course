from rest_framework import generics
from users.models import User
from users.serializers import UserSerializer

class UserCreateAPIView(generics.CreateAPIView):
    """ Create new user"""

    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    """ Users List """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """ User detail """

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    """ User update"""

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    """ User delete """

    queryset = User.objects.all()