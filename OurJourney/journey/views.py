from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
from .models import Adventures


# Create your views here.
def home(request):

    context = {
    }
    return render(request, 'journey/base.html', context)


class AdventureList(ListView):
    model = Adventures
    template_name = 'journey/search_adventures.html'
    context_object_name = 'adventure_list'
    paginate_by = 12


class AdventureDetail(DetailView):
    model = Adventures
    template_name = 'journey/detail.html'


def add_adventure(request):

    context = {

    }
    return render(request, 'journey/add_adventure.html', context)
