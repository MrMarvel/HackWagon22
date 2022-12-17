from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse


def audio_to_xml(request: WSGIRequest) -> HttpResponse:
    print("hi")
    return HttpResponse("hi")