from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, blank=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    sku = models.CharField(max_length=20, blank=False)
    inventory_count = models.IntegerField()
    is_active = models.BooleanField(default=True)
    #collection 
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)