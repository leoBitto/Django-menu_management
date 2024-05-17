from django.contrib import admin
from .models import DishType, Allergen, Menu, Dish, QuantityIngredient

@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_order')
    search_fields = ('name',)
    ordering = ('display_order',)

@admin.register(Allergen)
class AllergenAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Menu)
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
    list_display = ('dish', 'ingredient', 'quantity')
    search_fields = ('dish__name', 'ingredient__name')
    list_filter = ('dish__menu', 'ingredient')
