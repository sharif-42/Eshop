from rest_framework.pagination import PageNumberPagination


class BasePageNumberPagination(PageNumberPagination):
    # Use different pagination for different list apis
    page_size = 20
    page_size_query_param = 'page_size'
