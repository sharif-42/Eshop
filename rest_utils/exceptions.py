from django.http import Http404
from django.utils.translation import gettext_lazy as _
from rest_framework.response import Response
from rest_framework import exceptions, status
from rest_framework.exceptions import (
    APIException,
    MethodNotAllowed,
    NotFound,
    ValidationError,
)


# TODO: We will refactor it later
class BaseException(Exception):
    """
    Internal exception base class that can be handled by the exception handler.
    """
    code = None
    error_details = None
    message = None
    context = None
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(self, message="", context=None, code=None, error_details=None, *args, **kwargs):
        self.code = code or self.code
        self.error_details = error_details or self.error_details
        self.message = message or self.message or ""
        self.context = context or {}

        if kwargs:
            self.context.update(kwargs)

        if self.context and self.message:
            self.message = self.message.format(**self.context)

    def __str__(self):
        return str(self.message)


class BadRequestException(BaseException):
    status_code = status.HTTP_400_BAD_REQUEST
    code = "BAD_REQUEST"


class NotFoundException(BaseException):
    status_code = status.HTTP_404_NOT_FOUND
    code = "NOT_FOUND"
