from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class CustomLoginForm(AuthenticationForm):
    """
    Formulario para el inicio de sesión. Se usa AuthenticationForm de Django.
    """
    
    # Campo para el nombre de usuario
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "id": "username",
            "class": "form-control",
            "style": "width: 50%"
        })
    )

    # Campo para la contraseña e incluye función para visualizar la contraseña o ocultarla
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "id": "password",
            "class": "form-control",
            "style": "width: 10%"
        })
    )

class CustomUserCreationForm(UserCreationForm):
    """
    Formulario para el registro de usuarios usando UserCreationForm de Django.
    """
    
    # Campo para el email del usuario con validación.
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "id": "email",
            "class": "form-control",
            "style": "width: 10%;"
        })
    )
    
    class Meta:
        """
        Clase para configurar el modelo y campos del formulario
        """

        # username: nombre de usuario
        # email: correo electrónico
        # password1: contraseña
        # password2: confirmación de contraseña
        model = User
        fields = {'username', 'email', 'password1', 'password2'}
    
    def save(self, commit=True):
        """
        Método para guardar los datos ingresado por el usuario.
        
        Parámetros:
            commit (bool): Si es True, se guarda el usuario creado en la base de datos integrada con Django,
                         Si es False, solo crea la instancia sin guardarla.
        
        Retorna:
            User: Usuario creado
        """
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']  # Asigna el email al usuario
        
        if commit:
            user.save()  # Guarda el usuario en la base de datos
        
        return user