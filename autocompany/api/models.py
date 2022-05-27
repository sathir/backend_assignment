from django.db import models

class Product(models.Model):
    item_code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
