from django.urls import include, path
from rest_framework import routers
from .views import CollectionViewSet

router = routers.DefaultRouter()
router.register(r'collections', CollectionViewSet)

urlpatterns = [
    path('v1/', include(router.urls))
]

