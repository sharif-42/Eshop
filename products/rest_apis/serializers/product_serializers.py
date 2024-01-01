from rest_framework import serializers

from products.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'code',
            'name',
            'is_active',
            'short_description',
            'pre_order',
        ]
