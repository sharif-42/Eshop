from rest_framework import status, generics
from rest_framework.response import Response

from products.services import ProductService
from products.rest_apis.serializers import (
    ProductListSerializer,
    ProductDetailsSerializer,
)
from common.paginations import BasePageNumberPagination


class ProductListApiView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    service_class = ProductService
    pagination_class = BasePageNumberPagination

    def list(self, request, *args, **kwargs):
        product_list = self.service_class().get_active_product_list()

        page = self.paginate_queryset(product_list)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.serializer_class(product_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductDetailsApiView(generics.RetrieveAPIView):
    serializer_class = ProductDetailsSerializer
    service_class = ProductService

    def get(self, request, *args, **kwargs):
        product = self.service_class().get_product_by_code(code=kwargs.get('code'), use_cache=True)
        response = self.serializer_class(product).data
        return Response(response, status=status.HTTP_200_OK)
