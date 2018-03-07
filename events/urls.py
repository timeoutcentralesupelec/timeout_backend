from django.urls import path

from events.views import views
from events.views.event_list import EventList

urlpatterns = [
    path('', views.index, name='index'),
    path(r'all', EventList.as_view(), name='all')
]
