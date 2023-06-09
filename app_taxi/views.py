from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def handle_hello_world(req):
    return HttpResponse("hehe")
