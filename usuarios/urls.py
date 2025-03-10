from django.urls import path
from .views import registro, login_view, logout_view, inicio

urlpatterns = [
    path('', inicio, name='inicio'),
    path('registro/', registro, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]