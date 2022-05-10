from datetime import date, datetime, timezone
import imp
from msilib.schema import Class
from rest_framework.generics import ListAPIView, CreateAPIView

from recordapi.serializers import FishSerializer
from recordapi.models import Fish


class FishList(ListAPIView):
    queryset = Fish.objects.all().order_by('-uploaded')
    serializer_class = FishSerializer

class FishCreate(CreateAPIView):
    serializer_class = FishSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
