from django import views
from django.urls import path
from .views import registro, iniciar_sesion, cerrar_sesion

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('inicio/', views.inicio, name='inicio'),
    path('login/', iniciar_sesion, name='login'),
    path('logout/', cerrar_sesion, name='logout'),
]