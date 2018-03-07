import json

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import serializers

from events.models import Event


def index(request):
    return HttpResponse("Page des events")

def all(request):
    queryset = Event.objects.all()
    data = serializers.serialize('json', queryset)
    return HttpResponse(json.dumps(data), content_type='application/json')
