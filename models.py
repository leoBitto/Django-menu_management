from django.db import models
from django.utils.translation import gettext_lazy as _
from pdv_management.models import PDV

class DishType(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Nome"))
    display_order = models.IntegerField(default=0, verbose_name=_("Ordinamento"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Tipo di piatto")
        verbose_name_plural = _("Tipi di piatto")
        ordering = ['display_order']

class Dish(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Nome"))
    procedure = models.TextField(verbose_name=_("Procedimento"))
    dish_type = models.ForeignKey(DishType, on_delete=models.SET_NULL, null=True, verbose_name=_("Tipo"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Piatto")
        verbose_name_plural = _("Piatti")

class AbstractMenu(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Nome"))
    description = models.TextField(blank=True, verbose_name=_("Descrizione"))
    pdv = models.ForeignKey(PDV, related_name='%(class)s_menus', on_delete=models.CASCADE, verbose_name=_("PDV"))
    dishes = models.ManyToManyField(Dish, related_name='%(class)s_dishes', verbose_name=_("Piatti"))

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class PDVMenu(AbstractMenu):
    class Meta:
        verbose_name = _("Menu PDV")
        verbose_name_plural = _("Menu PDV")

class EventMenu(AbstractMenu):
    event_date = models.DateField(verbose_name=_("Data evento"))
    number_of_guests = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        verbose_name = _("Menu Evento")
        verbose_name_plural = _("Menu Eventi")

class QuantityIngredient(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, verbose_name=_("Piatto"))
    quantity = models.CharField(max_length=50, verbose_name=_("Quantità"))

    class Meta:
        verbose_name = _("Quantità Ingrediente")
        verbose_name_plural = _("Quantità Ingredienti")
