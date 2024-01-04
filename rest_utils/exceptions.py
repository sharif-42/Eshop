from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import (
    APIException,
    MethodNotAllowed,
    NotFound,
    ValidationError,
)


class BaseException(Exception):
    """
    Internal exception base class that can be handled by the exception handler.
    """
    default_code = None
    default_detail = None
    errors = []
    context = None
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(self, message="", context=None, default_code=None, errors=None, *args, **kwargs):
        self.default_code = default_code or self.default_code
        self.default_detail = message or self.default_detail or ""
        self.errors = errors or self.errors
        self.context = context or {}

        if kwargs:
            self.context.update(kwargs)

        if self.context and self.default_detail:
            self.message = self.default_detail.format(**self.context)

    def __str__(self):
        return str(self.default_detail)


class BadRequestException(BaseException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "BAD_REQUEST"


class NotFoundException(BaseException):
    status_code = status.HTTP_404_NOT_FOUND
    default_code = "NOT_FOUND"


class InvalidInputException(BadRequestException):
    default_code = "INVALID_INPUT"


def custom_exception_handler(exc, context=None):
    """
    Returns the response that should be used for any given exception.
    Example:
    {
        "message": "Object Not Found!",
        "error_code": "BAD_REQUEST",
        "errors": [
            "error1",
            "error2"
        ]
    }
    Any unhandled exceptions are caught and logged by this handler and
    an `OperationException` is raised accordingly the view or process behind that triggered the actual error.
    """
    # Always working with an APIException/Custom Created exception
    if not isinstance(exc, (APIException, BaseException)):
        raise exc

    if isinstance(exc, Http404):
        exc = NotFound()
    elif isinstance(exc, ValidationError):
        exc = InvalidInputException(errors=exc.detail)

    error_code = getattr(exc, "default_code", "OPERATION_FAILED").upper()       # default is OPERATION_FAILED
    message = getattr(exc, "default_detail", "Operation Failed")                # default is "Operation Failed"
    errors = getattr(exc, "errors", [])

    if isinstance(exc, MethodNotAllowed):
        error_code = "NOT_ALLOWED"
    elif isinstance(exc, NotFound):
        error_code = "NOT_FOUND"

    data = dict(message=message, error_code=error_code, errors=errors)
    return Response(data, status=exc.status_code)
