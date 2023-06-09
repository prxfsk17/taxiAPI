from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def handle_main_page(request : HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return handle_main_get(request)
    elif request.method == "POST":
        return handle_main_post(request)
    else:
        return HttpResponseNotAllowed("invalid request")

def handle_main_get(request : HttpRequest) -> HttpResponse:
    return HttpResponse("hehe")

def handle_main_post(request : HttpRequest) -> HttpResponse:
    return HttpResponse("hehe2")


