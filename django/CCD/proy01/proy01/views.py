# MyEnterprise/views.py

from django.shortcuts import HttpResponse

# Funciones para el manejo de vistas


def index(request):
    return HttpResponse('<h1>Bienvenido a Proy01 s.a.</h1>')
