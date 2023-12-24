from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models.base import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=256, help_text=_("Name of product."))
    short_description = models.TextField(
        help_text=_("Short summary, can be used in search results."),
        blank=True,
        default="",
    )
    long_description = models.TextField(
        help_text=_("Long Description"), blank=True, default=""
    )
    valid_from = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("Valid from"),
        help_text=_("Enter the datetime from which the product is valid"),
    )
    valid_until = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("Valid until"),
        help_text=_("Enter the datetime on which the product's validity expires"),
    )
    pre_order = models.BooleanField(
        default=False,
        verbose_name=_("Product is a pre-order product"),
        help_text=_('Can be pre ordered')
    )

    class Meta:
        indexes = [
            models.Index(fields=["code",]),
            models.Index(fields=["code", "is_active"]),
        ]

    def __str__(self):
        return f"{self.code}-{self.name}"
