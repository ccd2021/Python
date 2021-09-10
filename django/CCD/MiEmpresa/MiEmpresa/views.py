from django.shortcuts import HttpResponse

# Funciones para el manejo de vistas


def index(request, nombre):
    # return HttpResponse(f'<h1>Bienvenido a MiEmpresa s.a. señor {nombre}</h1>')
    return HttpResponse(f'<h1>Bienvenido a MiEmpresa s.a. señor {nombre}</h1>')
