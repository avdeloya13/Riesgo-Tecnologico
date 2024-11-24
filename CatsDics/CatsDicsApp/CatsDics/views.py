from urllib import request
from django import forms
from django.shortcuts import redirect, render

from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomLoginForm
from django.contrib.auth.models import User,Group, Permission

from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

def home(request):
    if request.user.is_authenticated:
        return redirect('homeLogin')  # Si ya inicio sesion manda al usuario de nuevo a HomeLogin
    return render(request, "home.html")

@login_required
def homeLogin(request):
    username = request.user.username if request.user.is_authenticated else None
    return render(request, "home.html", {'username': username})

@login_required
def log_Out(request):
    logout(request) 
    return redirect('home')

class CustomLoginView(LoginView):
    template_name = "login.html"
    form_class = CustomLoginForm

    def get_success_url(self):
        # Redirige a home si el inicio de sesión es correcto
        return reverse_lazy('homeLogin')

    def form_invalid(self, form):
        # Mantiene el formulario inválido en la misma página
        return super().form_invalid(form)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('homeLogin')  # Redirige a la página de inicio si ya está autenticado
        return super().get(request, *args, **kwargs)  # Llama al método `get` de la clase base

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homeLogin')
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homeLogin')
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()

    return render(request, 'login', {'form': form})

def productos(request):
    # Add your view logic here
    return render(request, 'productos.html')
