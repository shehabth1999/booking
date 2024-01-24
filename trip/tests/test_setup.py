from rest_framework.test import APITestCase
from faker import Faker
from trip.models import  Trip, Area
from authentication.models import User
from django.utils import timezone


class TestSetUp(APITestCase):

    def setUp(self):
        self.fake = Faker()
        self.user_data = {
            'email': self.fake.email(),
            'username': self.fake.email().split('@')[0],
            'password': self.fake.email(),
        }
        self.user = User.objects.create(**self.user_data)
        self.from_area = Area.objects.create(name='From Area')
        self.to_area = Area.objects.create(name='To Area', )

        self.trip_data = {
            'user': self.user,
            'name': 'Test Trip',
            'description': 'A test trip',
            'from_area': self.from_area,
            'to_area': self.to_area,
            'start_time': timezone.now(),
            'end_time': timezone.now(),
            'bus_number': '123ABC',
            'status': 1,
            'price': 100,
        }
        self.trip_updated_data = {
            'user': self.user.id,
            'name': 'Test Trip updated',
            'description': 'A test trip updated',
            'from_area': self.from_area.id,
            'to_area': self.to_area.id,
            "start_time": "2020-12-13T16:08:35+02:00",
            "end_time": "2017-12-13T13:17:21+02:00",
            'bus_number': '123ABC updated',
            'status': 2,
            'price': 150,
        }
        self.trip = Trip.objects.create(**self.trip_data)
        data_to_login = {'email': 'ali@ali.com', 'password': 'Ali123456'}
        response = self.client.post('/auth/login/', data_to_login, format='json')

        self.access = response.json()['tokens']['access']
        self.headers = {'HTTP_AUTHORIZATION': f'Bearer {self.access}'}



        # # Perform requests with the token
        self.list = self.client.get('/trip/api/',**self.headers)
        self.create = self.client.post('/trip/api/', data=self.trip_updated_data, **self.headers)
        self.read = self.client.get(f'/trip/api/{self.trip.id}/', **self.headers)
        self.update = self.client.put(f'/trip/api/{self.trip.id}/', data=self.trip_updated_data, **self.headers)
        self.delete = self.client.delete(f'/trip/api/{self.trip.id}/', **self.headers)

        return super().setUp()

    def tearDown(self):
        
        return super().tearDown()
