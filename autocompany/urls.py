"""autocompany URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from autocompany.api import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'api/v1/cart', views.ShoppingCartItemViewSet, basename='shopping-cart')
router.register(r'api/v1/order/items', views.OrderItemViewSet, basename='order-item')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # Product
    path('api/v1/products/', views.ProductListView.as_view()),
    path('api/v1/product/new/', views.ProductCreateView.as_view()),
    path('api/v1/product/<int:id>/',
         views.ProductRetrieveUpdateDestroyView.as_view()
         ),
    # Client
    path('api/v1/clients/', views.ClientListView.as_view()),
    path('api/v1/client/new/', views.ClientCreateView.as_view()),
    path('api/v1/client/<int:id>/',
         views.ClientRetrieveUpdateDestroyView.as_view()
         ),
    # ShoppingCartItem
    path('api/v1/cart/add/', views.ShoppingCartItemCreateView.as_view()),
    # Order
    path('api/v1/order/new/', views.OrderCreateView.as_view()),
    path('api/v1/order/<int:id>/',
         views.OrderRetrieveUpdateDestroyView.as_view()
         ),
    # OrderItem
    path('api/v1/order/item/add/', views.OrderItemCreateView.as_view()),
    path('api/v1/order/item/<int:id>/',
         views.OrderItemRetrieveUpdateDestroyView.as_view()
         ),
]
