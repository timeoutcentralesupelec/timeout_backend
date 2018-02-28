from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world !")

def event(request):
    return HttpResponse("Page des events")