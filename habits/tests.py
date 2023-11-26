from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email='test@test.com',
            password='test',
            is_staff=True,
            is_superuser=True
        )
        self.user.set_password('test')
        self.user.save()

        self.access_token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        self.habit = Habit.objects.create(
            user=self.user,
            action='test_action',
            start='2023-11-21T21:00:00',
            frequency=1,
            time_to_complete='00:01:00',
            place='test_place'

        )

        self.habit.save()

    def test_create_habit(self):
        data = {
            'action': self.habit.action,
            'start': self.habit.start,
            'frequency': self.habit.frequency,
            'time_to_complete': self.habit.time_to_complete,
            'place': self.habit.place,
            'user': self.user
        }
        response = self.client.post(
            '/habits/create/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            response.json(),
            {
                'id': (self.habit.id + 1),
                'action': self.habit.action,
                'start': self.habit.start,
                'frequency': self.habit.frequency,
                'next_reminder_date': None,
                'time_to_complete': self.habit.time_to_complete,
                'place': self.habit.place,
                'user': self.user.id,
                'related_habit': None,
                'reward': None,
                'is_public': False,
                'is_pleasant': False
            }
        )
        self.assertTrue(
            Habit.objects.all().exists()
        )

    def test_list_habit(self):
        response = self.client.get(
            '/habits/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json()['results'],
            [
                {'id': self.habit.id,
                 'action': self.habit.action,
                 'start': self.habit.start,
                 'frequency': self.habit.frequency,
                 'next_reminder_date': None,
                 'time_to_complete': self.habit.time_to_complete,
                 'place': self.habit.place,
                 'user': self.user.id,
                 'related_habit': None,
                 'reward': None,
                 'is_public': False,
                 'is_pleasant': False
                 }]
        )

    def test_retrieve_habit(self):
        response = self.client.get(
            f'/habits/{self.habit.id}/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {
                'id': self.habit.id,
                'action': self.habit.action,
                'start': self.habit.start,
                'frequency': 1,
                'next_reminder_date': None,
                'time_to_complete': self.habit.time_to_complete,
                'place': 'test_place',
                'user': self.user.id,
                'related_habit': None,
                'reward': None,
                'is_public': False,
                'is_pleasant': False
            }
        )

    def test_update_habit(self):
        data = {
            'action': 'Test_updated_habit',
            'start': self.habit.start,
            'frequency': self.habit.frequency,
            'time_to_complete': self.habit.time_to_complete
        }
        response = self.client.patch(
            f'/habits/update/{self.habit.id}/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {
                'id': self.habit.id,
                'action': 'Test_updated_habit',
                'start': self.habit.start,
                'frequency': self.habit.frequency,
                'next_reminder_date': None,
                'time_to_complete': self.habit.time_to_complete,
                'place': 'test_place',
                'user': self.user.id,
                'related_habit': None,
                'reward': None,
                'is_public': False,
                'is_pleasant': False
            }
        )

    def test_destroy_habit(self):
        response = self.client.delete(
            f'/habits/delete/{self.habit.id}/',
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_RelatedHabitOrRewardValidator(self):
        data = {
            'action': self.habit.action,
            'start': self.habit.start,
            'frequency': self.habit.frequency,
            'time_to_complete': self.habit.time_to_complete,
            'place': self.habit.place,
            'user': self.user,
            'related_habit': 'test_testov',
            'reward': 'test_reward'
        }
        response = self.client.post(
            path='/habits/create/',
            data=data
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
        self.assertEquals(
            response.json(),
            {
                'non_field_errors':
                    ['Необходимо выбрать связанную привычку ИЛИ вознаграждение',
                     'Связанная привычка может быть ТОЛЬКО приятной']
            }
        )

    def test_TimeToCompleteLimitationValidator(self):
        data = {
            'action': self.habit.action,
            'start': self.habit.start,
            'frequency': self.habit.frequency,
            'time_to_complete': '120',
            'place': self.habit.place,
            'user': self.user,
            'reward': 'test_reward'
        }
        response = self.client.post(
            path='/habits/create/',
            data=data
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
        self.assertEquals(
            response.json(),
            {
                'non_field_errors':
                    ['Время выполнения привычки НЕ должно превышать 120 секунд']
            }
        )

    def test_RelatedHabitValidation(self):
        self.habit.is_pleasant = False
        self.habit.save()
        data = {
            'action': self.habit.action,
            'start': self.habit.start,
            'frequency': self.habit.frequency,
            'time_to_complete': self.habit.time_to_complete,
            'place': self.habit.place,
            'user': self.user,
            'related_habit': self.habit.id
        }
        response = self.client.post(
            path='/habits/create/',
            data=data
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
        self.assertEquals(
            response.json(),
            {
                'non_field_errors':
                    ['Связанная привычка может быть ТОЛЬКО приятной']
            }
        )

    def test_PleasantHabitValidation(self):
        data = {
            'action': self.habit.action,
            'start': self.habit.start,
            'frequency': self.habit.frequency,
            'time_to_complete': self.habit.time_to_complete,
            'place': self.habit.place,
            'user': self.user,
            'reward': 'test_reward',
            'is_pleasant': True
        }
        response = self.client.post(
            path='/habits/create/',
            data=data
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
        self.assertEquals(
            response.json(),
            {
                'non_field_errors':
                    ['Приятная привычка НЕ может иметь вознаграждения']
            }
        )

    def test_FrequencyValidation(self):
        data = {
            'action': self.habit.action,
            'start': self.habit.start,
            'frequency': 8,
            'time_to_complete': self.habit.time_to_complete,
            'place': self.habit.place,
            'user': self.user,
            'reward': 'test_reward',
        }
        response = self.client.post(
            path='/habits/create/',
            data=data
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
        self.assertEquals(
            response.json(),
            {
                'non_field_errors':
                    ['Привычка должна выполняться НЕ реже 1 раза в неделю']
            }
        )
