from rest_framework import viewsets
from .models import Studio, Reservation
from .serializers import StudioSerializer, ReservationSerializer
import logging

logger = logging.getLogger(__name__)

class StudioViewSet(viewsets.ModelViewSet):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer
    
    def list(self, request, *args, **kwargs):
        logger.info("Received request for Studio list")
        return super().list(request, *args, **kwargs)

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
