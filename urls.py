from django.urls import path
from . import views

app_name = 'menu_management'

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('wine/', views.wine, name='wine'),

    path('dashboard/dishtypes/', views.dishtype_dashboard, name='dishtype_dashboard'),
    path('dashboard/dishtypes/add/', views.dishtype_add, name='dishtype_add'),
    path('dashboard/dishtypes/<int:dishtype_id>/edit/', views.dishtype_update, name='dishtype_update'),
    path('dashboard/dishtypes/<int:dishtype_id>/delete/', views.dishtype_delete, name='dishtype_delete'),
    
    # URL per la gestione dei piatti
    path('dashboard/dishes/', views.dish_dashboard, name='dish_dashboard'),
    path('dashboard/dishes/<int:dish_id>/', views.dish_detail, name='dish_detail'),
    path('dashboard/dishes/add/', views.dish_add, name='dish_add'),
    path('dashboard/dishes/<int:dish_id>/edit/', views.dish_update, name='dish_update'),
    path('dashboard/dishes/<int:dish_id>/delete/', views.dish_delete, name='dish_delete'),


    path('dashboard/menu/', views.menu_dashboard, name='menu_dashboard'),
    path('dashboard/menu/add/', views.menu_add, name='menu_add'),
    path('dashboard/menu/update/<int:menu_id>/', views.menu_update, name='menu_update'),
    path('dashboard/menu/delete/<int:menu_id>/', views.menu_delete, name='menu_delete'),
]
