from django.contrib import admin
from .models import Adventures, TakenAdventures

# Register your models here.
admin.site.register(Adventures)
admin.site.register(TakenAdventures)
