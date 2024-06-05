from django import forms
from django.utils.translation import gettext_lazy as _
from .models import *


class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = ['name', 'display_order']
        labels = {
            'name': _('Nome'),
            'display_order': _('Ordine di presentazione'),
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'display_order': forms.NumberInput(attrs={'style': 'width:6ch'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': _('Inserisci il nome')})
        self.fields['display_order'].widget.attrs.update({'placeholder': _('Inserisci la posizione di presentazione')})



class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'procedure', 'dish_type', 'price']
        labels = {
            'name': _('Nome'),
            'procedure': _('Ricetta'),
            'dish_type': _('Tipo di Piatto'),
            'price': _('Prezzo di vendita'),
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'procedure': forms.Textarea(attrs={'class': 'form-control', 'rows': 3,}),
            'dish_type': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'style': 'width:6ch'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': _('Inserisci il nome')})
        self.fields['procedure'].widget.attrs.update({'placeholder': _('Inserisci la ricetta')})
        self.fields['dish_type'].widget.attrs.update({'placeholder': _('Inserisci il tipo di piatto')})
        self.fields['price'].widget.attrs.update({'placeholder': _('Inserisci il prezzo')})



class MenuForm(forms.ModelForm):
    class Meta:
        model = PDVMenu
        fields = ['name', 'description', 'pdv', 'dishes']
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



class EventMenuForm(forms.ModelForm):
    class Meta:
        model = EventMenu
        fields = ['name', 'description', 'pdv', 'dishes', 'event_date', 'number_of_guests', 'price_per_person']
        labels = {
            'name': _('Nome'),
            'description': _('Descrizione'),
            'pdv': _('PDV'),
            'event_date': _('Data evento'),
            'number_of_guest': _('Numero di persone'),
            'price_per_person': _('Prezzo a persona'),
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'pdv': forms.Select(attrs={'class': 'form-control'}),
            'event_date': forms.DateInput(format=('%Y-%m-%d'),
                    attrs={'class': 'form-control', 'placeholder': 'Seleziona una data', 'type': 'date'}),
            'number_of_guest': forms.NumberInput(attrs={'style': 'width:6ch'}),
            'price_per_person': forms.NumberInput(attrs={'style': 'width:6ch'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': _('Inserisci il nome')})
        self.fields['description'].widget.attrs.update({'placeholder': _('Inserisci la descrizione')})




class QuantityIngredientForm(forms.ModelForm):
    class Meta:
        model = QuantityIngredient
        fields = ['dish', 
                  #'ingredient', 
                  'quantity']
        labels = {
            'dish': _('Piatto'),
            #'ingredient': _('Ingrediente'),
            'quantity': _('Quantità'),
        }
        widgets = {
            'dish': forms.Select(attrs={'class': 'form-control'}),
           # 'ingredient': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quantity'].widget.attrs.update({'placeholder': _('Inserisci la quantità')})
