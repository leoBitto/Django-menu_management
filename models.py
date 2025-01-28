from django.db import models
from django.utils.translation import gettext_lazy as _

class VersionedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    version = models.IntegerField(default=1)  # Versione dell'oggetto
    previous_version = models.OneToOneField(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='next_version'
    )
    is_current = models.BooleanField(default=True)  # Flag per identificare la versione corrente
    is_deleted = models.BooleanField(default=False)  # Soft delete flag

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.pk:  # Modifica di un oggetto esistente
            if self.is_current:  # Solo la versione corrente può essere aggiornata
                # Disabilita la versione corrente
                self.is_current = False
                self.save(update_fields=['is_current'])

                # Crea una nuova versione
                new_version_data = {
                    field.name: getattr(self, field.name)
                    for field in self._meta.fields
                    if field.name not in ['id', 'created_at', 'updated_at', 'version', 'is_current', 'is_deleted']
                }
                new_version_data.update({
                    'version': self.version + 1,
                    'previous_version': self,
                    'is_current': True,
                })
                return self.__class__.objects.create(**new_version_data)
            else:
                raise ValueError("Modifiche permesse solo alla versione corrente.")
        else:
            # Creazione di un nuovo oggetto
            super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """Soft delete dell'oggetto."""
        self.is_deleted = True
        self.is_current = False
        self.save(update_fields=['is_deleted', 'is_current'])

    @classmethod
    def get_current_version(cls, **filters):
        """Recupera l'ultima versione corrente e non eliminata."""
        return cls.objects.filter(is_current=True, is_deleted=False, **filters)


class DishType(models.TextChoices):
    ENTREE = 'entree', _('Antipasto')
    FIRST_DISH = 'first_dish', _('Primo piatto')
    SECOND_DISH = 'second_dish', _('Secondo piatto')
    SIDE_DISH = 'side_dish', _('Contorno')
    DESSERT = 'dessert', _('Dessert')
    OTHER = 'other', _('Altro')


class Dish(VersionedModel):
    name = models.CharField(
        max_length=100,
        null=True,
        verbose_name=_('Dish Name'),
        help_text=_('Name of the dish, e.g., Spaghetti Carbonara')
    )
    price = models.CharField(
        max_length=50,
        null=True,
        verbose_name=_('Price'),
        help_text=_('Price of the dish with units, e.g., "14 euro a persona"')
    )
    dish_type = models.CharField(
        max_length=20,
        choices=DishType.choices,
        verbose_name=_('Dish Type'),
        help_text=_('Category of the dish, e.g., Antipasto or Primo piatto')
    )

    def __str__(self):
        return self.name
