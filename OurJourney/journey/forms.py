from django import forms
from .models import Adventures


class AddAdventureForm(forms.ModelForm):
    class Meta:
        model = Adventures
        fields = ['adventure', 'category', 'subcategory', 'location', 'hours', 'website', 'details', 'image']
