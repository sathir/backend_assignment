from rest_framework import serializers

from autocompany.api.models import Product, Client, ShoppingCartItem, Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "item_code", "name", "description", "unit_price"]


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "customer_code", "first_name", "last_name", "pref_name", "gender", "mobile_number", "email"]


class ShoppingCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCartItem
        fields = ["id", "client", "product", "quantity", "delivery_fee"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["client", "address", "delivery_date"]


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["order", "product", "quantity"]