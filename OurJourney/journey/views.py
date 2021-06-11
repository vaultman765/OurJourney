from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
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


# Class based view for create_item
class AddAdventure(CreateView):
    model = Adventures
    # Only fields in form
    fields = ['adventure', 'category', 'subcategory', 'location', 'hours', 'website', 'details', 'image']
    template_name = 'journey/adventure_form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)
