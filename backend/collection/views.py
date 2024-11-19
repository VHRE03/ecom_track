from rest_framework import viewsets
from .serializer import CollectionSerializer
from .models import Collection

class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all().order_by('id')
    serializer_class = CollectionSerializer