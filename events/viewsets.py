# Viewsets allow us to concentrate on modelling the state and interactions of the API, and leave the URL construction to be handled automatically

from .models import Event
from rest_framework import viewsets
from .serializers import EventSerializer

# If we want a filter from a foreign key (asso here)
# class FilterByAsso(object):
#     def get_queryset(self):   #You need to override the default get_queryset method
#         queryset = super().get_queryset()
#         asso_id = self.request.query_params.get('asso-id')

#         # This filters the queryset by asso (if there is a asso)
#         if asso_id is not None:
#             queryset = queryset.filter(asso=asso_id)

#         return queryset

class EventViewSet(viewsets.ModelViewSet): # Add FilterByAsso in the classes EventViewSet inherits from if needed
    queryset = Event.objects.all()
    serializer_class = EventSerializer
