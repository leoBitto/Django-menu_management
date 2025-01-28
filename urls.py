from django.urls import path
from . import views

app_name = 'menu_management'

urlpatterns = [
    path('', views.MenuView.as_view(), name='menu'),
    path('wine/', views.WineView.as_view(), name='wine'),
    path('backoffice/', views.DishView.as_view(), name='menu_backoffice'),
    path('backoffice/dish/<int:pk>/', views.DishView.as_view(), name='dish_action'),
]