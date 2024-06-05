from django.urls import path
from . import views

app_name = 'menu_management'

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('wine/', views.wine, name='wine'),

    path('menu_dashboard/', views.menu_dashboard, name='menu_dashboard'),

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


    #path('menu_dashboard/add_dish/', views.add_dish, name='add_dish'),
    #path('menu_dashboard/update_dish/<int:dish_id>/', views.update_dish, name='update_dish'),
    #path('menu_dashboard/delete_dish/<int:dish_id>/', views.delete_dish, name='delete_dish'),
#
    #path('menu_dashboard/add_dish_type/', views.add_dish_type, name='add_dish_type'),
    #path('menu_dashboard/update_dish_type/<int:dish_id>/', views.update_dish_type, name='update_dish_type'),
    #path('menu_dashboard/delete_dish_type/<int:dish_id>/', views.delete_dish_type, name='delete_dish_type'),
#
    ##path('menu_dashboard/add_menu/', views.add_menu, name='add_menu'),
    #path('menu_dashboard/update_menu/<int:menu_id>/', views.update_menu, name='update_menu'),
    #path('menu_dashboard/delete_menu/<int:menu_id>/', views.delete_menu, name='delete_menu'),
#
    #path('menu_dashboard/add_menu_event/', views.add_menu_event, name='add_menu_event'),
    #path('menu_dashboard/update_menu_event/<int:menu_event_id>/', views.update_menu_event, name='update_menu_event'),
    #path('menu_dashboard/delete_menu_event/<int:menu_event_id>/', views.delete_menu_event, name='delete_menu_event'),
]
