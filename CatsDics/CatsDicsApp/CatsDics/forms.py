from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth.models import User

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget= forms.TextInput(attrs = { "id":"username",
    "class":"form-control", "style": "width: 50%" }))

    password = forms.CharField(widget= forms.PasswordInput(attrs = { "id":"password",
    "class":"form-control", "style": "width: 10%" }))

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(widget= forms.EmailInput(attrs = { "id": "email",
    "class":"form-control", "style": "width: 10%;" }))

    class Meta:
        model = User
        fields = {'username', 'email', 'password1', 'password2'}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user