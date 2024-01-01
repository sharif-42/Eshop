from rest_utils.exceptions import NotFoundException
from django.utils.translation import gettext_lazy as _


class ProductNotFoundException(NotFoundException):
    code = "PRODUCT_NOT_FOUND"
    message = _("product not found.")
