from django.shortcuts import render, HttpResponse

# Create your views here.


def newApp(response):
    return HttpResponse("Esta es la nueva App")
