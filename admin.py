from django.contrib import admin
from .models import DishType, PDVMenu, EventMenu, Dish, QuantityIngredient

@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_order')
    search_fields = ('name',)
    ordering = ('display_order',)


@admin.register(EventMenu)
class MenuEventAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_date', 'pdv', 'number_of_guests')
    search_fields = ('name',)
    list_filter = ('pdv',)


@admin.register(PDVMenu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'pdv')
    search_fields = ('name',)
    list_filter = ('pdv',)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu', 'dish_type')
    search_fields = ('name', 'menu__name')
    list_filter = ('menu', 'dish_type')

@admin.register(QuantityIngredient)
class QuantityIngredientAdmin(admin.ModelAdmin):
    list_display = ('dish', 'quantity')
    search_fields = ('dish__name', 'ingredient__name')
    list_filter = ('dish__menu',)
