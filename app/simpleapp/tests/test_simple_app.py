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

    def test_calculate_success1(self):
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