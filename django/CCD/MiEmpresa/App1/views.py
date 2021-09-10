from django.shortcuts import render, HttpResponse

# Create your views here.


# def bienvenida_app(request):
#    return HttpResponse("<h1> Bienvenido a la primera aplicación de MiEmpresa </h1>")


# def bienvenida_app(request):
#    return render(request, "index.html")  # Utilizamos la función render

def bienvenida_app(request, nombre):

    contexto = {
        'nombre': nombre,
        'amigos': ['Hernan', 'Alejandro', 'Roberto']
    }
    # return HttpResponse("<h1> Bienvenido a la primera aplicacion de mi Empresa </h1>")
    return render(request, "index.html", contexto)


def solicitudes(request):  # Vista que detecta solicitudes GET y POST
    context = {}
    if request.method == "GET":
        print("Se detectó una solicitud GET")
        print(request.GET)
        context['solicitud'] = 'GET'
    elif request.method == "POST":
        print("Se detectó una solicitud POST")
        print(request.POST)
        context['solicitud'] = 'POST'
    return render(request, "solicitudes.html", context)


def form(request):  # Vista para formulario que genera solicitudes POST
    return render(request, "form.html")


'''
def bienvenida_app(request):
    
    contexto = {
        'nombre': 'Carlos Alberto',
        'amigos': ['Hernan', 'Alejandro', 'Roberto']
    }
    # return HttpResponse("<h1> Bienvenido a la primera aplicacion de mi Empresa </h1>")
    return render(request, "index.html", contexto)

'''
