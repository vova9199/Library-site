from django import forms
from .models import Author  # Import the Author model from your app

class AuthorCreateForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'surname', 'patronymic']

class AuthorEditForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'surname', 'patronymic']