# App1/urls.py
from django.urls import path
from App1 import views

urlpatterns = [
    path('bienvenida_app/<str:nombre>', views.bienvenida_app),
    path('solicitudes/', views.solicitudes),
    path('formulario/', views.form),

    #path('bienvenida_app/', views.bienvenida_app),
    #path('solicitudes/', views.solicitudes),
    #path('formulario/', views.form),
]
