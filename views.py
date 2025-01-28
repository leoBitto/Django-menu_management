from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import View
from .forms import DishForm
from .models import Dish, DishType

class MenuView(View):
    template_name = 'menu_management/menu.html'

    def get(self, request, *args, **kwargs):
        dishes_by_type = {
            dish_type: Dish.get_current_version(dish_type=dish_type)
            for dish_type in DishType.values
        }

        context = {
            'dishes_by_type': dishes_by_type,
            'title': 'Il nostro Menù',
        }
        return render(request, self.template_name, context)

class WineView(View):
    template_name = 'menu_management/wine.html'

    def get(self, request, *args, **kwargs):
        context = {
            'title': 'Il nostro Vino',
        }
        return render(request, self.template_name, context)

class DishView(LoginRequiredMixin, View):
    template_name = 'menu_management/backoffice/menu_backoffice.html'

    def get(self, request, *args, **kwargs):
        context = {
            'dish_data': self._get_dish_data(),
            'dish_form': DishForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        action = request.POST.get('action', 'create')
        
        if action == 'create':
            return self._handle_create(request)
        
        dish_id = kwargs.get('pk')
        if not dish_id:
            messages.error(request, 'ID piatto mancante.')
            return redirect('menu_management:menu_backoffice')
            
        dish = get_object_or_404(Dish, id=dish_id, is_deleted=False)
        
        handlers = {
            'update': self._handle_update,
            'delete': self._handle_delete
        }
        
        handler = handlers.get(action)
        if not handler:
            messages.error(request, 'Azione non valida.')
            return redirect('menu_management:menu_backoffice')
            
        return handler(request, dish)

    def _get_dish_data(self):
        """Recupera i dati dei piatti organizzati per tipo."""
        return {
            dish_type: [
                {
                    'dish': dish,
                    'form': DishForm(instance=dish),
                }
                for dish in Dish.get_current_version(dish_type=dish_type[0])
            ]
            for dish_type in DishType.choices
        }

    def _handle_create(self, request):
        """Gestisce la creazione di un nuovo piatto."""
        form = DishForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Piatto aggiunto con successo.')
            except Exception as e:
                messages.error(request, f'Errore durante il salvataggio: {str(e)}')
        else:
            self._add_form_errors(form)
        return redirect('menu_management:menu_backoffice')

    def _handle_update(self, request, dish):
        """Gestisce l'aggiornamento di un piatto esistente."""
        form = DishForm(request.POST, instance=dish)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Piatto aggiornato con successo.')
            except ValueError as e:
                messages.error(request, f'Errore durante l\'aggiornamento: {str(e)}')
        else:
            self._add_form_errors(form)
        return redirect('menu_management:menu_backoffice')

    def _handle_delete(self, request, dish):
        """Gestisce l'eliminazione soft di un piatto."""
        try:
            dish.delete()
            messages.success(request, 'Piatto eliminato con successo.')
        except Exception as e:
            messages.error(request, f'Errore durante l\'eliminazione: {str(e)}')
        return redirect('menu_management:menu_backoffice')

    def _add_form_errors(self, form):
        """Aggiunge gli errori del form ai messaggi."""
        error_message = ', '.join(
            f'{field}: {error}' 
            for field, errors in form.errors.items() 
            for error in errors
        )
        messages.error(request, f'Si è verificato un errore: {error_message}')