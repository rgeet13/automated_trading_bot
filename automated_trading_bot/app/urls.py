from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ScannersDataViewset, AuthCodeViewSet, OrderPlacementViewset

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'scanner', ScannersDataViewset, basename='scanner')
router.register(r'authcodes', AuthCodeViewSet, basename='authcodes')
router.register(r'order', OrderPlacementViewset, basename='order')
# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
