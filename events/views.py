from django.http import HttpResponse
from django.shortcuts import render

def event(request):
    return HttpResponse("Page des events")
