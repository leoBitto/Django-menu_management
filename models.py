from django.db import models
from django.utils.translation import gettext_lazy as _
from pdv_management.models import PDV
from inventory.models import Ingredient

class DishType(models.TextChoices):
    name = models.CharField(max_length=100, verbose_name=_("Nome"))
    display_order = models.IntegerField(default=0, verbose_name=_("Ordinamento"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Tipo di piatto")
        verbose_name_plural = _("Tipi di piatto")
        ordering = ['display_order']


class Allergen(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Nome"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Allergene")
        verbose_name_plural = _("Allergeni")

class Menu(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Nome"))
    description = models.TextField(blank=True, verbose_name=_("Descrizione"))
    pdv = models.ForeignKey(PDV, related_name='menus', on_delete=models.CASCADE, verbose_name=_("PDV"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Menu")
        verbose_name_plural = _("Menu")

class Dish(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Nome"))
    procedure = models.TextField(verbose_name=_("Procedimento"))
    menu = models.ForeignKey(Menu, related_name='dishes', on_delete=models.CASCADE, verbose_name=_("Menu"))
    dish_type = models.CharField(max_length=20, choices=DishType.choices, verbose_name=_("Tipo"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Piatto")
        verbose_name_plural = _("Piatti")

class QuantityIngredient(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, verbose_name=_("Piatto"))
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, verbose_name=_("Ingrediente"))
    quantity = models.CharField(max_length=50, verbose_name=_("Quantità"))

    class Meta:
        verbose_name = _("Quantità Ingrediente")
        verbose_name_plural = _("Quantità Ingredienti")
