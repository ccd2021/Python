# Create your views here.
from django.db.models.fields import EmailField
from django.shortcuts import redirect, render

from .models import User
# Create your views here.


def index(request):
    return render(request, 'index.html')


def register_user(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:  # method == 'POST'
        # Creacion de un usuario
        name = request.POST['name']
        lastname = request.POST['lastname']
        correo_electronico = request.POST['email']
        password = request.POST['password']
        new_user = User.objects.create(
            name=name, lastname=lastname, email=correo_electronico, password=password)

        print('usuario creado:', new_user.name)
        request.session['username'] = new_user.name

        return redirect('/home')


def home(request):
    return render(request, 'home.html')
