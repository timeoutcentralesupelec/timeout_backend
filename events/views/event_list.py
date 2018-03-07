from rest_framework import generics

from events.models import Event
from events.serializers.event import EventSerializer


class EventList(generics.ListAPIView) :
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.all()
        return queryset