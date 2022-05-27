from rest_framework import serializers

from autocompany.api.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "item_code", "name", "description", "unit_price"]