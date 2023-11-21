from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import User


class UserTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email='test@test.com',
            password='test',
            is_staff=True,
            is_superuser=True,
            is_active=True,
            phone='+79850979779',
            chat_id=9999999

        )
        self.user.set_password('test')
        self.user.save()

        self.access_token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_retrieve_user(self):
        response = self.client.get(
            f'/users/{self.user.id}/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {
                'chat_id': self.user.chat_id,
                'email': self.user.email,
                'first_name': '',
                'groups': [],
                'id': self.user.id,
                'is_staff': self.user.is_staff,
                'is_superuser': self.user.is_superuser,
                'last_name': '',
                'phone': self.user.phone,
                'user_permissions': []
            }
        )

    def test_list_user(self):
        response = self.client.get(
            '/users/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json()['results'],
            [
                {'chat_id': self.user.chat_id,
                 'email': self.user.email,
                 'first_name': '',
                 'groups': [],
                 'id': self.user.id,
                 'is_staff': self.user.is_staff,
                 'is_superuser': self.user.is_superuser,
                 'last_name': '',
                 'phone': self.user.phone,
                 'user_permissions': []
                 }]
        )

    def test_update_user(self):
        self.user.is_superuser = False
        self.user.save()
        data = {
            'chat_id': self.user.chat_id,
            'email': self.user.email,
            'first_name': '',
            'groups': [],
            'id': self.user.id,
            'is_staff': self.user.is_staff,
            'is_superuser': self.user.is_superuser,
            'last_name': '',
            'phone': self.user.phone,
            'user_permissions': []
        }
        response = self.client.patch(
            f'/users/update/{self.user.id}/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {
                'chat_id': self.user.chat_id,
                'email': self.user.email,
                'first_name': '',
                'groups': [],
                'id': self.user.id,
                'is_staff': self.user.is_staff,
                'is_superuser': False,
                'last_name': '',
                'phone': self.user.phone,
                'user_permissions': []
            }
        )

    def user_destroy_habit(self):
        response = self.client.delete(
            f'/users/destroy/{self.user.id}/',
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
