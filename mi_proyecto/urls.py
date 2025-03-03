from django.contrib import admin
from django.urls import path
from usuarios import views
from usuarios.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Definir la URL de inicio
    path('', inicio, name='inicio'),
    
    # Autenticación
    path('usuarios/registro/', views.registro, name='registro'),
    path('usuarios/login/', views.login_view, name='login'),
    path('usuarios/logout/', views.logout_view, name='logout'),
]