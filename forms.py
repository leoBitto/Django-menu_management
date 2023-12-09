# forms.py
from django import forms
from .models import *

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'price', 'dish_type']
        widgets = {
            'dish_type': forms.HiddenInput(),  # Rendi il campo dish_type nascosto
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Inserisci il nome'})
        self.fields['price'].widget.attrs.update({'placeholder': 'Inserisci il prezzo'})

