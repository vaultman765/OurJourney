from . import views
from django.urls import path

app_name = 'journey'
urlpatterns = [
    # /journey/
    path('', views.home, name='home'),
    path('search_adventures/', views.AdventureList.as_view(), name='search_adventures'),
    path('add_adventure/', views.add_adventure, name='add_adventure')
]
