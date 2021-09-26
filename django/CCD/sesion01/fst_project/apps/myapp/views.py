#from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

# Enrutamiento


def index(request):
    # return HttpResponse("Hola Django")
    return render(request, "index.html")


def home_usuario(request):
    return render(request, 'home_usuario.html')


# Enrutamiento con parametros.
def hello_user(request, username):
    context = {'username_HTML': username}
    return render(request, 'hola_usuario.html', context)


def repetir(request, username, repeticiones):
    context = {'username_HTML': username,
               'repeticiones_HTML': range(repeticiones)}
    return render(request, 'repeticiones.html', context)
