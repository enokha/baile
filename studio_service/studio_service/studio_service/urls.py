from django.urls import path, include
from rest_framework.routers import DefaultRouter
from studios.views import StudioViewSet

router = DefaultRouter()
router.register(r'studios', StudioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
