from django.urls import path
from . import views

app_name = 'menu_management'

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('wine/', views.wine, name='wine'),

    path('menu_dashboard/', views.menu_dashboard, name='menu_dashboard'),

    path('add_dish/', views.add_dish, name='add_dish'),
    path('update_dish/<int:dish_id>/', views.update_dish, name='update_dish'),
    path('delete_dish/<int:dish_id>/', views.delete_dish, name='delete_dish'),
]
