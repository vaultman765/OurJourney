from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

app_name = 'journey'
urlpatterns = [
    # /journey/
    path('', views.home, name='home'),
    path('search_adventures/', views.AdventureList.as_view(), name='search_adventures'),
    path('add_adventure/', views.add_adventure, name='add_adventure'),
    path('<int:pk>/', views.AdventureDetail.as_view(), name='detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
