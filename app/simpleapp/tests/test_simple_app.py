"""
Test for simple app
"""
from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

SIMPLE_URL = reverse('simpleapp:calculate')

class SimpleAppTest(TestCase):
    """test api in simple app"""

    def setUp(self):
        self.client = APIClient()

    def test_calculate_success(self):
        """calculate 1 + 1 = 2"""
        payload = {
            'x': 1,
            'y': 1,
        }

        result = self.client.post(SIMPLE_URL, payload)

        # compare status
        self.assertEqual(result.status_code, status.HTTP_200_OK)

        # compare data
        self.assertEqual(result.data, {'result':2})

    def test_calculate_success2(self):
        """"calculate 10 + 25 = 35"""
        payload = {
            'x': 10,
            'y': 25,
        }

        result = self.client.post(SIMPLE_URL, payload)

        # compare status
        self.assertEqual(result.status_code, status.HTTP_200_OK)

        # compare data
        self.assertEqual(result.data, {'result':35})

    def test_calculate_fail(self):
        """calculate 5 + 'a' """
        payload = {
            'x': 5,
            'y': 'a',
        }

        result = self.client.post(SIMPLE_URL, payload)

        # compare status
        self.assertEqual(result.status_code, status.HTTP_400_BAD_REQUEST)

    def test_calculate_fail2(self):
        """calculate 'b' + 50 """
        payload = {
            'x': 'b',
            'y': 50,
        }

        result = self.client.post(SIMPLE_URL, payload)

        # compare status
        self.assertEqual(result.status_code, status.HTTP_400_BAD_REQUEST)

    def test_calculate_fail3(self):
        """calculate 'a' + 'b' """
        payload = {
            'x': 'a',
            'y': 'b',
        }

        result = self.client.post(SIMPLE_URL, payload)

        # compare status
        self.assertEqual(result.status_code, status.HTTP_400_BAD_REQUEST)