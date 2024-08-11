from django.urls import include, path
from rest_framework.routers import DefaultRouter

from advertisements.views import AdvertisementViewSet

router = DefaultRouter()
router.register(r'advertisements', AdvertisementViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
