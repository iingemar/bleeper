from django.db.models import Q

from rest_framework import generics

from app_name.models import Bleep
from .serializers import BleepModelSerializer


class BleepListAPIView(generics.ListAPIView):
    serializer_class = BleepModelSerializer

    def get_queryset(self, *args, **kwargs):
        qs = Bleep.objects.all()
        print(self.request.GET)
        # Query defaults to None
        query = self.request.GET.get('q', None)
        print(query)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return qs