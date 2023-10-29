from django import forms
from .models import Book
from author.models import Author

class BookForm(forms.ModelForm):
    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        widget=forms.SelectMultiple(attrs={'size': '5'}),
        required=True
    )

    class Meta:
        model = Book
        fields = ['name', 'description', 'count', 'authors']

class BookEditForm(forms.ModelForm):
    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        widget=forms.SelectMultiple(attrs={'size': '5'}),
        required=True
    )

    class Meta:
        model = Book
        fields = '__all__'