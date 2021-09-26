from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("This method is the second view in app_two")
