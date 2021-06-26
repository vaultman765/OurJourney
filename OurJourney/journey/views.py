from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Adventures, TakenAdventures
from datetime import datetime, timedelta
from .google_calendar.cal_setup import get_calendar_service
from django.shortcuts import redirect
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    image_objects = TakenAdventures.objects.all()

    paginator = Paginator(image_objects, 1)
    page = request.GET.get('page')
    active_image = paginator.get_page(page)

    if active_image.has_next():
        next_page = active_image.next_page_number()
        next_image = paginator.get_page(next_page)
    else: 
        next_image = paginator.get_page(1)

    if active_image.has_previous():
        prev_page = active_image.previous_page_number()
        prev_image = paginator.get_page(prev_page)
    else: 
        prev_image = paginator.get_page(paginator.num_pages)

    context = {
        'prev_image': prev_image,
        'active_image': active_image,
        'next_image': next_image
    }
    return render(request, 'journey/home.html', context)


class AdventureList(ListView):
    model = Adventures
    template_name = 'journey/search_adventures.html'
    context_object_name = 'adventure_list'
    paginate_by = 12


# Class based view for create_item
class AddAdventure(CreateView):
    model = Adventures
    # Only fields in form
    fields = ['adventure', 'category', 'subcategory', 'location', 'hours', 'website', 'details', 'image']
    template_name = 'journey/adventure_form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)


def calendar(request):

    context = {
    }
    return render(request, 'journey/calendar.html', context)


def detail(request, id):
    adv = Adventures.objects.get(id=id)

    if request.method == "POST":
        summary = request.POST.get('adventure', "")
        description = request.POST.get('details', "")
        sdate = request.POST.get('sdate', "")
        stime = request.POST.get('stime', "")
        hours = request.POST.get('hours', "")
        location = request.POST.get('', "")

        start = sdate+stime
        start_dt = datetime.strptime(start, '%Y-%m-%d%I:%M%p')
        end_dt = start_dt + timedelta(hours=float(hours))

        start_dt = start_dt.isoformat()
        end_dt = end_dt.isoformat()

        service = get_calendar_service()
        service.events().insert(calendarId='primary',
                                body={
                                   "summary": summary,
                                   "description": description,
                                   "start": {"dateTime": start_dt, "timeZone": 'America/New_York'},
                                   "end": {"dateTime": end_dt, "timeZone": 'America/New_York'},
                                   "location": location
                                }).execute()

    return render(request, 'journey/detail.html', {'adv': adv})


def home_redirect(request):
    return redirect('/journey/')


