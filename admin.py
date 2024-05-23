from django.contrib import admin
from .models import DishType, Dish, PDVMenu, EventMenu, QuantityIngredient

class DishTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_order')
    ordering = ('display_order',)

class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'dish_type')
    search_fields = ('name', 'procedure')
    list_filter = ('dish_type',)

class QuantityIngredientInline(admin.TabularInline):
    model = QuantityIngredient
    extra = 1

class PDVMenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'pdv')
    search_fields = ('name', 'description')
    list_filter = ('pdv',)
    filter_horizontal = ('dishes',)

class EventMenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'pdv', 'event_date', 'number_of_guests')
    search_fields = ('name', 'description')
    list_filter = ('pdv', 'event_date')
    filter_horizontal = ('dishes',)

admin.site.register(DishType, DishTypeAdmin)
admin.site.register(Dish, DishAdmin)
admin.site.register(PDVMenu, PDVMenuAdmin)
admin.site.register(EventMenu, EventMenuAdmin)
