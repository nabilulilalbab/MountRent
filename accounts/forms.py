from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'user'
        if commit:
            user.save()
        return user

class MitraRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','no_hp', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'mitra'
        user.no_hp = self.cleaned_data.get('no_hp')
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    pass
