from rest_framework import generics

from events.models import Event
from events.serializers.event import EventSerializer

class FilterByAsso(object):

    def get_queryset(self):
        queryset = super().get_queryset()
        asso_id = self.request.query_params.get('asso')

        # This filters the queryset by asso (if there is an asso)
        if asso_id is not None:
            queryset = queryset.filter(city=asso_id)

        return queryset

class EventList(FilterByAsso, generics.ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    # def get_queryset(self):
    #     queryset = Event.objects.all()
    #     return queryset
