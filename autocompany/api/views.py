from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination

from autocompany.api.models import Product, Client
from autocompany.api.serializers import ProductSerializer, ClientSerializer

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
            cache.delete('pet_data_{}'.format(product_id))
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            product = response.data
            cache.set('pet_data_{}'.format(product['id']), {
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
    search_fields = ('name', 'description')

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
            cache.delete('pet_data_{}'.format(client_id))
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            client = response.data
            cache.set('pet_data_{}'.format(client['id']), {
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