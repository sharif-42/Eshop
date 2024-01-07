import pytest
from django.conf import settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


# urls/views for tests
PRODUCT_LIST_URL = reverse(f"{settings.API_VERSION_NAMESPACE}:product:products")
PRODUCT_DETAILS_URL = reverse(f"{settings.API_VERSION_NAMESPACE}:product:product-details", kwargs={"code": "factory-test"})

# We need this to save instance to test DB. Otherwise, We can't save the instance to model.
pytestmark = pytest.mark.django_db


@pytest.fixture
def new_product(db, product_factory):
    # FactoryBoy Provide us two builds in strategy one just use the object or save it to test database
    # for 1st strategy we call method build and for second we call method create
    # product_obj = product_factory.build()  # this will create object instance
    # product_obj = product_factory.create()  # this will create instance in test DB.

    product_obj = product_factory.create()
    return product_obj


class TestProductListAPI:

    def test_product_list_api_for_empty_product(self):
        response = APIClient().get(PRODUCT_LIST_URL)

        assert response.status_code == status.HTTP_200_OK
        assert "next" in response.data
        assert "previous" in response.data
        assert response.data['count'] == 0

    def test_product_list_api_for_containing_product(self, new_product):
        response = APIClient().get(PRODUCT_LIST_URL)
        data = response.json()["results"][0]

        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1

        assert "next" in response.data
        assert "previous" in response.data
        assert data.get("code") == "factory-test"


class TestProductDetailsAPI:

    def test_product_details_api_for_empty_product(self):

        response = APIClient().get(PRODUCT_DETAILS_URL)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_product_details_api_for_existing_product(self, new_product):

        response = APIClient().get(PRODUCT_DETAILS_URL)

        assert response.status_code == status.HTTP_200_OK
        assert "product_type" in response.data
        assert "product_group" in response.data
        assert "brand" in response.data
        assert response.data.get("code") == "factory-test"

