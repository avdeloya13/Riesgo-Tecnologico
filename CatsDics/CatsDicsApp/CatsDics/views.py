# Vistas para las plantillas de la página

from urllib import request
from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomLoginForm
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

def home(request):
    """
    Vista principal de la página CatDics.

    Parámetros:
        request: HttpRequest object

    Retorna:
        HttpResponse: Renderiza home.html o redirige a homeLogin
    """
    if request.user.is_authenticated:
        return redirect('homeLogin')
    return render(request, "home.html")

@login_required
def homeLogin(request):
    """
    Vista protegida para usuarios autenticados, se requiere primero haber iniciado de sesión.

    Parámetros:
        request: HttpRequest object

    Retorna:
        HttpResponse: Renderiza home.html con el contexto del usuario
    """
    username = request.user.username if request.user.is_authenticated else None
    return render(request, "home.html", {'username': username})

@login_required
def log_Out(request):
    """
    Vista para cerrar sesión, se requiere haber iniciado de sesión y redirige al inicio de sesión.

    Parámetros:
        request: HttpRequest object

    Retorna:
        HttpResponse: Redirige a la vista 'homeLogin'
    """
    logout(request)
    return redirect('homeLogin')

class CustomLoginView(LoginView):
    """
    Vista para el inicio de sesión, se usa LoginView de Django para personalizar el comportamiento
    del inicio de sesión.
    """

    template_name = "login.html"
    form_class = CustomLoginForm

    def get_success_url(self):
        """
        Define la URL de redirección después de un inicio de sesión exitoso.

        Retorna:
            str: URL de redirección
        """
        return reverse_lazy('homeLogin')

    def form_invalid(self, form):
        """
        Maneja el caso de formulario inválido cuando se ingresa datos erroneos.

        Parámetros:
            form: Formulario con datos inválidos por el usuario

        Retorna:
            HttpResponse: Respuesta con formulario inválido
        """
        return super().form_invalid(form)

    def get(self, request, *args, **kwargs):
        """
        Maneja las peticiones GET a la vista de login.

        Parámetros:
            request: HttpRequest object
            *args: Argumentos posicionales
            **kwargs: Argumentos nombrados

        Retorna:
            HttpResponse: Redirige a homeLogin o muestra formulario
        """
        if request.user.is_authenticated:
            return redirect('homeLogin')
        return super().get(request, *args, **kwargs)

def register(request):
    """
    Vista para el registro de nuevos usuarios.

    Parámetros:
        request: HttpRequest object

    Retorna:
        HttpResponse: Renderiza register.html o redirige a homeLogin
    """
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
    """
    Segunda opción de metodo para el inicio de sesión.

    Parámetros:
        request: HttpRequest object

    Retorna:
        HttpResponse: Renderiza login.html o redirige a homeLogin
    """
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

# No esta acabado
def productos(request):
    """
    Vista para visualizar los producto en la página una vez el usuario inicio seseión.

    Parámetros:
        request: HttpRequest object

    Retorna:
        HttpResponse: Renderiza productos.html
    """
    return render(request, 'productos.html')