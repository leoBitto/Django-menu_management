from django.db import models
from django.utils.translation import gettext as _

class DishType(models.TextChoices):
    ENTREE = 'entree', _('Antipasto')
    FIRST_DISH = 'first_dish', _('Primo piatto')
    SECOND_DISH = 'second_dish', _('Secondo piatto')
    SIDE_DISH = 'side_dish', _('Contorno')
    DESSERT = 'dessert', _('Dessert')
    OTHER = 'other', _('Altro')


class Dish(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.CharField(max_length=10, null=True)
    dish_type = models.CharField(max_length=20, choices=DishType.choices)

    def __str__(self):
        return self.name




