from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination

from autocompany.api.models import Product, Client, ShoppingCartItem, OrderItem, Order
from autocompany.api.serializers import ProductSerializer, ClientSerializer, ShoppingCartItemSerializer, \
    OrderItemSerializer, OrderSerializer


class Pagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 100

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id',)
    search_fields = ('name', 'description')

class ProductCreateView(CreateAPIView):
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    lookup_field = 'id'
    serializer_class = ProductSerializer

    def delete(self, request, *args, **kwargs):
        product_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('product_data_{}'.format(product_id))
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            product = response.data
            cache.set('product_data_{}'.format(product['id']), {
                'item_code' : product['name'],
                'name' : product['name'],
                'description' : product['description'],
                'unit_price' : product['unit_price'],
                'description' : product['description'],
                'created_at' : product['created_at'],
                'updated_at' : product['updated_at'],
            })
        return response


class ClientListView(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id',)
    search_fields = ('customer_code', 'first_name', 'last_name', 'pref_name', 'mobile_number', 'email',)

class ClientCreateView(CreateAPIView):
    serializer_class = ClientSerializer


class ClientRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    lookup_field = 'id'
    serializer_class = ClientSerializer

    def delete(self, request, *args, **kwargs):
        client_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('client_data_{}'.format(client_id))
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            client = response.data
            cache.set('client_data_{}'.format(client['id']), {
                'customer_code' : client['customer_code'],
                'first_name' : client['first_name'],
                'last_name' : client['last_name'],
                'pref_name' : client['pref_name'],
                'gender' : client['gender'],
                'mobile_number' : client['mobile_number'],
                'email' : client['email'],
                'created_at': client['created_at'],
                'updated_at': client['updated_at'],
            })
        return response


class ShoppingCartItemCreateView(CreateAPIView):
    serializer_class = ShoppingCartItemSerializer


class ShoppingCartItemRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ShoppingCartItem.objects.all()
    lookup_field = 'id'
    serializer_class = ShoppingCartItemSerializer

    def delete(self, request, *args, **kwargs):
        shopping_cart_item_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('shopping_cart_item_data_{}'.format(shopping_cart_item_id))
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            shopping_cart_item = response.data
            cache.set('shopping_cart_item_data_{}'.format(shopping_cart_item['id']), {
                'client' : shopping_cart_item['client'],
                'product' : shopping_cart_item['product'],
                'quantity' : shopping_cart_item['quantity'],
            })
        return response


class OrderCreateView(CreateAPIView):
    serializer_class = OrderItemSerializer


class OrderRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    lookup_field = 'id'
    serializer_class = OrderSerializer

    def delete(self, request, *args, **kwargs):
        order_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('order_data_{}'.format(order_id))
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            order = response.data
            cache.set('order_item_data_{}'.format(order['id']), {
                'order_number' : order['order_number'],
                'address' : order['address'],
                'delivery_date' : order['delivery_date'],
                'delivery_fee': order['delivery_fee'],
            })
        return response


class OrderItemCreateView(CreateAPIView):
    serializer_class = OrderItemSerializer


class OrderItemRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    lookup_field = 'id'
    serializer_class = OrderItemSerializer

    def delete(self, request, *args, **kwargs):
        order_item_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('order_item_data_{}'.format(order_item_id))
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            order_item = response.data
            cache.set('order_item_data_{}'.format(order_item['id']), {
                'order' : order_item['order'],
                'product' : order_item['product'],
                'quantity' : order_item['quantity'],
            })
        return response