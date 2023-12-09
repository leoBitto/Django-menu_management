# Esempio di views per la gestione dei piatti
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import DishForm
from .models import *
from django.contrib.auth.decorators import login_required
from website.models import Contact

## menu
def menu(request):

    entrees = Dish.objects.filter(dish_type=DishType.ENTREE)
    first_dishes = Dish.objects.filter(dish_type=DishType.FIRST_DISH)
    second_dishes = Dish.objects.filter(dish_type=DishType.SECOND_DISH)
    side_dishes = Dish.objects.filter(dish_type=DishType.SIDE_DISH)
    desserts = Dish.objects.filter(dish_type=DishType.DESSERT)
    others = Dish.objects.filter(dish_type=DishType.OTHER)


    contact = Contact.objects.first()

    context={
        'entrees':entrees,
        'first_dishes':first_dishes,
        'second_dishes':second_dishes,
        'side_dishes':side_dishes,
        'desserts':desserts,
        'others':others,
        'title':'Il nostro Menù',
        'phone':contact.phone,
    }

    return render(request, 'menu_management/menu.html', context)

## menu
def wine(request):
    contact = Contact.objects.first()
    context={
        'title':'Il nostro Vino',
        'phone':contact.phone,
    }

    return render(request, 'menu_management/wine.html', context)


# VIEWS PER MENU
###
# this view show the menu on the dashboard
###
@login_required
def menu_dashboard(request):

    dish_form = DishForm()
    
    dish_types = DishType.choices
    dish_data = {}
    
    for dish_type in dish_types:
        
        dishes = Dish.objects.filter(dish_type=dish_type[0])

        # Creare una lista per ogni categoria di piatti
        dish_data[dish_type] = []

        for dish in dishes:
            dish_form_instance = get_object_or_404(Dish, id=dish.id)
            dish_data[dish_type].append({
                'dish': dish,
                'form': DishForm(instance=dish_form_instance),
            })

    context = {        

        'dish_data': dish_data,
        'dish_form':dish_form,
    }

    return render(request, 'menu_management/dashboard/menu_dashboard.html', context)


@login_required
def add_dish(request):
    if request.method == 'POST':
        form = DishForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Piatto aggiunto con successo.')
            return redirect('menu_management:menu_dashboard')
        else:
            messages.error(request, 'Si è verificato un errore. Si prega di correggere il modulo.')
            return render(request, 'menu_management/dashboard/menu_dashboard.html', {'form': form})
    else:
        form = DishForm()
        return render(request, 'menu_management/dashboard/menu_dashboard.html', {'form': form})


@login_required
def update_dish(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)

    if request.method == 'POST':
        form = DishForm(request.POST, instance=dish)
        if form.is_valid():
            form.save()
            messages.success(request, 'Piatto aggiornato con successo.')
            return redirect('menu_management:menu_dashboard')
        else:
            messages.error(request, 'Si è verificato un errore. Si prega di correggere il modulo.')
            return render(request, 'menu_management/dashboard/menu_dashboard.html', {'form': form})
    else:
        form = DishForm(instance=dish)
        return render(request, 'menu_management/dashboard/menu_dashboard.html', {'form': form})


@login_required
def delete_dish(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)

    dish.delete()
    messages.success(request, 'Piatto eliminato con successo.')
    return redirect('menu_management:menu_dashboard')


