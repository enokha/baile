from rest_framework.routers import DefaultRouter
from .views import StudioViewSet, ReservationViewSet

router = DefaultRouter()
router.register(r'studios', StudioViewSet)
router.register(r'reservations', ReservationViewSet)

urlpatterns = router.urls
