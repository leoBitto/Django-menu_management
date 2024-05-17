from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Menu, Dish, QuantityIngredient

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'description', 'pdv']
        labels = {
            'name': _('Nome'),
            'description': _('Descrizione'),
            'pdv': _('PDV'),
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Inserisci il nome')}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': _('Inserisci la descrizione')}),
            'pdv': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': _('Inserisci il nome')})
        self.fields['description'].widget.attrs.update({'placeholder': _('Inserisci la descrizione')})

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'procedure', 'menu', 'dish_type']
        labels = {
            'name': _('Nome'),
            'procedure': _('Procedimento'),
            'menu': _('Menu'),
            'dish_type': _('Tipo'),
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'procedure': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'menu': forms.Select(attrs={'class': 'form-control'}),
            'dish_type': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': _('Inserisci il nome')})
        self.fields['procedure'].widget.attrs.update({'placeholder': _('Inserisci il procedimento')})

class QuantityIngredientForm(forms.ModelForm):
    class Meta:
        model = QuantityIngredient
        fields = ['dish', 'ingredient', 'quantity']
        labels = {
            'dish': _('Piatto'),
            'ingredient': _('Ingrediente'),
            'quantity': _('Quantità'),
        }
        widgets = {
            'dish': forms.Select(attrs={'class': 'form-control'}),
            'ingredient': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quantity'].widget.attrs.update({'placeholder': _('Inserisci la quantità')})
