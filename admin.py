from django.contrib import admin
from .models import Dish
@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'dish_type')
    list_filter = ('dish_type',)
    search_fields = ('name',)


