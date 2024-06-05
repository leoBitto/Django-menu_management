# Esempio di views per la gestione dei piatti
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import DishForm, DishTypeForm
from .models import *
from django.contrib.auth.decorators import login_required


## menu
def menu(request):

    entrees = Dish.objects.filter(dish_type=DishType.ENTREE)
    first_dishes = Dish.objects.filter(dish_type=DishType.FIRST_DISH)
    second_dishes = Dish.objects.filter(dish_type=DishType.SECOND_DISH)
    side_dishes = Dish.objects.filter(dish_type=DishType.SIDE_DISH)
    desserts = Dish.objects.filter(dish_type=DishType.DESSERT)
    others = Dish.objects.filter(dish_type=DishType.OTHER)


    #contact = Contact.objects.first()

    context={
        'entrees':entrees,
        'first_dishes':first_dishes,
        'second_dishes':second_dishes,
        'side_dishes':side_dishes,
        'desserts':desserts,
        'others':others,
        'title':'Il nostro Menù',
        #'phone':contact.phone,
    }

    return render(request, 'menu_management/menu.html', context)

## menu
def wine(request):
    #contact = Contact.objects.first()
    context={
        'title':'Il nostro Vino',
        #'phone':contact.phone,
    }

    return render(request, 'menu_management/wine.html', context)


# VIEWS PER MENU
###
# this view show the menu on the dashboard
###


@login_required
def dishtype_dashboard(request):
    dishtype_form = DishTypeForm()
    dishtype_list = DishType.objects.all()
    dishtype_data = {}

    for dishtype in dishtype_list:
        dishtype_data[dishtype] = {
            'dishtype_instance': dishtype,
            'dishtype_form': DishTypeForm(instance=dishtype),
        }

    context = {
        'dishtype_data': dishtype_data,
        'dishtype_form': dishtype_form,
    }

    return render(request, 'menu_management/dashboard/dishtype_dashboard.html', context)

@login_required
def dishtype_add(request):
    if request.method == 'POST':
        dishtype_form = DishTypeForm(request.POST)

        if dishtype_form.is_valid():
            dishtype_form.save()
            messages.success(request, 'Tipologia di piatto aggiunta con successo.')
            return redirect('menu_management:dishtype_dashboard')
        else:
            for field, errors in dishtype_form.errors.items():
                for error in errors:
                    messages.error(request, f"Errore nel campo {field}: {error}")
            return redirect('menu_management:dishtype_dashboard')
    else:
        return redirect('menu_management:dishtype_dashboard')

@login_required
def dishtype_update(request, dishtype_id):
    dishtype = get_object_or_404(DishType, id=dishtype_id)

    if request.method == 'POST':
        dishtype_form = DishTypeForm(request.POST, instance=dishtype)
        if dishtype_form.is_valid():
            dishtype_form.save()
            messages.success(request, 'Tipologia di piatto aggiornata con successo.')
            return redirect('menu_management:dishtype_dashboard')
        else:
            for field, errors in dishtype_form.errors.items():
                for error in errors:
                    messages.error(request, f"Errore nel campo {field}: {error}")
            return redirect('menu_management:dishtype_dashboard')
    else:
        return redirect('menu_management:dishtype_dashboard')

@login_required
def dishtype_delete(request, dishtype_id):
    dishtype = get_object_or_404(DishType, id=dishtype_id)
    if request.method == 'POST':
        dishtype.delete()
        messages.success(request, 'Tipologia di piatto eliminata con successo.')
    else:
        messages.error(request, 'Si è verificato un errore. Si prega di riprovare.')
    return redirect('menu_management:dishtype_dashboard')



@login_required
def dish_dashboard(request):
    dish_form = DishForm()
    dish_list = Dish.objects.all()
    dish_data = {}

    for dish in dish_list:
        dish_data.setdefault(dish.dish_type, []).append({
            'dish_instance': dish,
        })

    context = {
        'dish_data': dish_data,
        'dish_form': dish_form,
    }

    return render(request, 'menu_management/dashboard/dish_dashboard.html', context)


@login_required
def dish_detail(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    dish_form = DishForm(instance=dish)
    return render(request, 'menu_management/dashboard/dish_detail.html', {'dish': dish, 'dish_form': dish_form})


@login_required
def dish_add(request):
    if request.method == 'POST':
        dish_form = DishForm(request.POST)
        if dish_form.is_valid():
            dish_form.save()
            messages.success(request, 'Piatto aggiunto con successo.')
            return redirect('menu_management:dish_dashboard')
        else:
            for field, errors in dish_form.errors.items():
                for error in errors:
                    messages.error(request, f"Errore nel campo {field}: {error}")
            return redirect('menu_management:dish_dashboard')
    else:
        return redirect('menu_management:dish_dashboard')

@login_required
def dish_update(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    if request.method == 'POST':
        dish_form = DishForm(request.POST, instance=dish)
        if dish_form.is_valid():
            dish_form.save()
            messages.success(request, 'Piatto aggiornato con successo.')
            return redirect('menu_management:dish_dashboard')
        else:
            for field, errors in dish_form.errors.items():
                for error in errors:
                    messages.error(request, f"Errore nel campo {field}: {error}")
            return redirect('menu_management:dish_dashboard')
    else:
        return redirect('menu_management:dish_dashboard')

@login_required
def dish_delete(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    if request.method == 'POST':
        dish.delete()
        messages.success(request, 'Piatto eliminato con successo.')
    else:
        messages.error(request, 'Si è verificato un errore. Si prega di riprovare.')
    return redirect('menu_management:dish_dashboard')













@login_required
def menu_dashboard(request):


    context = {        

 
    }

    return render(request, 'menu_management/dashboard/menu_dashboard.html', context)


