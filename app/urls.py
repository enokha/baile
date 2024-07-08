from django.urls import path, include
from rest_framework.routers import DefaultRouter
from studio_reservation.reservation.views import UserViewSet, StudioViewSet, ReservationViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'users', UserViewSet)  # User endpoints
router.register(r'studios', StudioViewSet)  # Studio endpoints
router.register(r'reservations', ReservationViewSet)  # Reservation endpoints

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),  # Enables login/logout in the browsable API
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Endpoint for token generation
    path('', include(router.urls)),  # Include all routes from the router
]