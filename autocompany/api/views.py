from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.pagination import LimitOffsetPagination

from autocompany.api.models import Product
from autocompany.api.serializers import ProductSerializer

class ProductPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 100

class ProductListViewSet(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id',)
    search_fields = ('name', 'description')

class ProductCreate(CreateAPIView):
    serializer_class = ProductSerializer