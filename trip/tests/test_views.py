from rest_framework import status
from .test_setup import TestSetUp


class TestTripView(TestSetUp):
    def test_add(self):
        self.assertEqual(1,1)
    
    def test_list_trips(self):
        response = self.list
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_trip(self):
        response = self.create
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_trip(self):
        response = self.read
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_trip(self):
        response = self.update
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_trip(self):
        response = self.delete
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
