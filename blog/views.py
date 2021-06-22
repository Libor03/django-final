from django.shortcuts import render

from django.views import generic
from .models import Type, Animal, Attachment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.contrib.auth.models import User  # Blog author or commenter
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.forms import AnimalForm
from django.urls import reverse_lazy


def index(request):
    """
    View function for home page of site.
    """
    num_animals = Animal.objects.all().count()

    # Do proměnné films se uloží 3 filmy uspořádané podle hodnocení (sestupně)
    animals = Animal.objects.order_by('name')[:3]

    """ Do proměnné context, která je typu slovník (dictionary) uložíme hodnoty obou proměnných """
    context = {
        'num_animals': num_animals,
        'animals': animals
    }
    # Render the HTML template index.html
    return render(
        request,
        'index.html',
        context=context
    )

class AnimalCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Animal
    fields = ['name', 'poster', 'latin', 'description']
    login_url = '/accounts/login/'
    permission_required = 'blog.add_animal'


class AnimalUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Animal
    template_name = 'update.html'
    form_class = AnimalForm
    login_url = '/accounts/login/'
    permission_required = 'blog.change_animal'

class AnimalDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Animal
    success_url = reverse_lazy('animals')
    login_url = '/accounts/login/'
    permission_required = 'blog.delete_animal'


class AnimalListView(generic.ListView):
    """
    Generic class-based view for a list of all blogs.
    """
    model = Animal
    paginate_by = 5
    context_object_name = 'animals'


class AnimalDetailView(generic.DetailView):
    """
    Generic class-based detail view for a blog.
    """
    model = Animal
    context_object_name = 'animal'


def error_400(request, exception=None):
    return render(request, 'errors/400.html')

def error_404(request, exception=None):
        return render(request, 'errors/404.html')


def error_500(request):
    return render(request, 'errors/500.html')


def error_403(request, exception=None):
    return render(request, 'errors/403.html')



