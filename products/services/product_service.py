from django.utils import timezone

from products.models import Product
from products.exceptions import ProductNotFoundException


class ProductService:
    model = Product

    def get_active_product_list(self):
        """
        Return the products those are available and active.
        """
        now = timezone.now()
        product_list = self.model.objects.filter(
            is_active=True, valid_from__lte=now, valid_until__gte=now
        )
        return product_list

    def get_product_by_code(self, code):
        try:
            return self.model.objects.get(code=code)
        except Product.DoesNotExist:
            raise ProductNotFoundException()
