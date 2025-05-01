from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


AIRPORT_URL = reverse("airport:airport-list")

class UnauthenticatedAirportApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        res = self.client.get(AIRPORT_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)