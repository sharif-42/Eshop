from rest_framework import status, generics
from rest_framework.response import Response

from products.services import ProductService
from products.rest_apis.serializers import (
    ProductListSerializer,
    # ProductDetailsSerializer,
)
from common.paginations import BasePageNumberPagination


class ProductListApiView(generics.ListAPIView):
    """
    This api will be consumed by FE
    """
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


# class ProductDetailsApiView(generics.RetrieveAPIView):
#     """
#     This api will be consumed by FE
#     """
#     serializer_class = ProductDetailsSerializer
#     service_class = ProductService
#
#     def get(self, request, *args, **kwargs):
#         code = kwargs.get('code')
#         cache_key = f"product-{code}"
#         cached_response = self.service_class().get_cached_product(cache_key=cache_key)
#         if cached_response:
#             response = cached_response
#         else:
#             product = self.service_class().get_product_by_code(code=code)
#             response = self.serializer_class(product).data
#             self.service_class().set_cache_product(cache_key=cache_key, product_response=response)
#         return Response(response, status=status.HTTP_200_OK)
