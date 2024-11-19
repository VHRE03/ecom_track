from django.db import models

class Collection(models.Model):
    name = models.CharField(max_length=250, blank=False)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)