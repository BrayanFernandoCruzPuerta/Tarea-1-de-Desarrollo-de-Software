from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm
from django.contrib.auth.forms import AuthenticationForm

def inicio(request):
    return render(request, 'usuarios/inicio.html')

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)  # Inicia sesión automáticamente
            return redirect('inicio')  # Redirige a la vista de inicio
        else:
            print("Errores en el formulario:", form.errors)
    else:
        form = RegistroForm()

    return render(request, 'usuarios/registro.html', {'form': form})

def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')  # Redirige a la página de inicio
        else:
            return render(request, 'usuarios/login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'usuarios/login.html', {'form': form})

@login_required
def logout_view(request):
    """ Cerrar sesión y redirigir al login """
    logout(request)
    return redirect('login')