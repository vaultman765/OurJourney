from django.shortcuts import render


# Create your views here.
def home(request):

    context = {
    }
    return render(request, 'journey/base.html', context)


def search_adventures(request):

    context = {

    }
    return render(request, 'journey/search_adventures.html', context)


def add_adventure(request):

    context = {

    }
    return render(request, 'journey/add_adventure.html', context)

