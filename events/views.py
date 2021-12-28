from django.shortcuts import render
from django.http import HttpRequest
from django.http import request

# Create your views here.

def events(request):
    return render (request, "events.html")