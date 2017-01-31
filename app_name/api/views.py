from rest_framework import generics

from app_name.models import Bleep
from .serializers import BleepModelSerializer


class BleepListAPIView(generics.ListAPIView):
    serializer_class = BleepModelSerializer

    def get_queryset(self):
        return Bleep.objects.all()