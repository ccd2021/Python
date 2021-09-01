#from django.db.models.fields import EmailField
from django.shortcuts import redirect, render

from .models import User


def index(request):
    return render(request, 'index.html')


def register_user(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:  # method == 'POST'
        # Creacion de un usuario
        name = request.POST['name']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        new_user = User.objects.create(
            name=name, lastname=lastname, email=email, password=password)

        print('Usuario creado:', new_user.name)
        request.session['username'] = new_user.name

        return redirect('/home')


def home(request):
    return render(request, 'home.html')
