from rest_framework import viewsets
from .serializer import ProductSerializer
from .models import Product

class ProductViewSet(viewsets.ModelViewSet):
    model = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer