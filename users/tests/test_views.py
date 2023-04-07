import pytest
from django.conf import settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from django.contrib.auth import get_user_model

pytestmark = pytest.mark.django_db


class TestUserListCreateAPI:

    def test_user_create_api(self):
        assert 1 == 1

    def test_user_list_api(self):
        assert 2 == 2