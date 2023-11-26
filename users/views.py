from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from habits.permissions import IsOwnerOrIsSuperuser, IsSuperuser
from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """ Create new user"""

    serializer_class = UserSerializer

    class Meta:
        model = User
        fields = '__all__'
        permission_classes = [IsAuthenticated]


class UserListAPIView(generics.ListAPIView):
    """ Users List """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    class Meta:
        model = User
        fields = '__all__'
        permission_classes = [IsAuthenticated, IsSuperuser]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """ User detail """

    serializer_class = UserSerializer
    queryset = User.objects.all()

    class Meta:
        model = User
        fields = '__all__'
        permission_classes = [IsAuthenticated, IsSuperuser]


class UserUpdateAPIView(generics.UpdateAPIView):
    """ User update"""

    serializer_class = UserSerializer
    queryset = User.objects.all()

    class Meta:
        model = User
        fields = '__all__'
        permission_classes = [IsAuthenticated, IsOwnerOrIsSuperuser]


class UserDestroyAPIView(generics.DestroyAPIView):
    """ User delete """

    queryset = User.objects.all()

    class Meta:
        model = User
        fields = '__all__'
        permission_classes = [IsAuthenticated, IsSuperuser]
