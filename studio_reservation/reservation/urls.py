from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudioViewSet, ReservationViewSet, UserViewSet

router = DefaultRouter()
router.register(r'studios', StudioViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'users', UserViewSet)  # Register the new route for users

urlpatterns = [
    path('', include(router.urls)),
]
