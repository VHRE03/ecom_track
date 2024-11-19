from django.db import models
from collection.models import Collection

class Product(models.Model):
    name = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    sku = models.CharField(max_length=20, blank=False)
    inventory_count = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.DO_NOTHING, null=False, blank=False)