from django import forms
from .models import Order
from portfolio.models import Works


class OrderForm(forms.ModelForm):
    order_works = forms.ModelChoiceField(queryset=Works.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Order
        fields = ['order_works', 'order_name', 'order_phone', 'order_email']

        # name = forms.CharField(label='Имя', max_length=150,
        #                        widget=forms.TextInput(attrs={'class': 'form-input', 'name': 'first_name'}))
        # phone = forms.CharField(label='Телефон', max_length=150, widget=forms.TextInput(attrs={'class': 'form-input'}))
        # email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-input'}))
