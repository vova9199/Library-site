from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import CustomUser


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'middle_name', 'last_name', 'email', 'password', 'role')



class CustomUserUpdateForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'middle_name', 'last_name', 'email', 'role', 'is_active')
        exclude = ['password']


class CustomLoginForm(AuthenticationForm):
    email = forms.EmailField(
        label="Email",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
    )
    password = forms.CharField(
        label="Password",
        strip=False,  # Allow leading/trailing whitespace
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
    )