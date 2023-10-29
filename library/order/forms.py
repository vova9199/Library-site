from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    plated_end_at = forms.DateTimeField(
        input_formats=['%Y-%m-%d %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',
            'class': 'form-control',
            'placeholder': 'YYYY-MM-DD HH:MM'
        }),
    )

    class BookChoiceField(forms.ModelChoiceField):
        def label_from_instance(self, obj):
            return obj.name

    class UserChoiceField(forms.ModelChoiceField):
        def label_from_instance(self, obj):
            return f"{obj.first_name} {obj.last_name}"  # або просто obj.first_name, якщо хочете показати тільки ім'я

    book = BookChoiceField(
        queryset=Order.book.field.related_model.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',
        }),
        empty_label="Оберіть книгу"
    )

    user = UserChoiceField(
        queryset=Order.user.field.related_model.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',
        }),
        empty_label="Оберіть користувача"
    )

    class Meta:
        model = Order
        fields = ['book', 'user', 'plated_end_at']

class OrderEditForm(OrderCreateForm):  # OrderEditForm може успадковувати властивості OrderCreateForm
    class Meta:
        model = Order
        fields = ['plated_end_at', 'book', 'user']
