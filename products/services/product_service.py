from django.core.cache import cache
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

    def get_cached_product(self, cache_key):
        cached_response = cache.get(cache_key)
        return cached_response

    def _get_product_by_code(self, code):
        """
        :param code:
        :return:
        """
        try:
            return self.model.objects.get(code=code)
        except Product.DoesNotExist:
            raise ProductNotFoundException(message=f"Product Not Found with code: '{code}'")

    def get_product_by_code(self, code, use_cache=False):
        """
        :param code: Product code
        :param use_cache: If true product will be searched on cache first.
        :return: Product object
        """
        product = None
        cache_key = f"product-{code}"
        if use_cache:
            cached_response = self.get_cached_product(cache_key=cache_key)
            if cached_response:
                product = cached_response
        if not product:
            # product not found in cache.
            product = self._get_product_by_code(code=code)
            # product found, now set the cache to use it later
            cache.set(cache_key, product, 60 * 60)

        return product
