from django import forms
from django.forms import NumberInput, TextInput

from coin.models import Coin


class CoinForm(forms.ModelForm):
    class Meta:
        model = Coin
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your coin name'}),
            'price': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your coin price'}),
            'market_cap': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your value'}),
            'volume': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your volume'}),
        }
