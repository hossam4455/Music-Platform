from urllib import response
from django.test import TestCase
from rest_framework import status
from rest_framework.test import RequestsClient


class UserTest(TestCase):
    fixtures=['users.yaml']