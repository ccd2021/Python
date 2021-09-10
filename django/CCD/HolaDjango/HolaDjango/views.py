from django.shortcuts import HttpResponse


def hola(response):
    return HttpResponse("Hola Mundo")
