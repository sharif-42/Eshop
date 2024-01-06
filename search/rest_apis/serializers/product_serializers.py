from rest_framework import serializers

from products.models import Product


class ProductSearchListOutputSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            "code",
            "name",
            "is_active",
            "short_description",
            "pre_order",
        ]
