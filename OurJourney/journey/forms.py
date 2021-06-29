from django import forms
from .models import Adventures


class AddAdventureForm(forms.ModelForm):
    class Meta:
        model = Adventures
        fields = ['adventure', 'category', 'subcategory', 'location', 'hours', 'website', 'details', 'image']


class LoginForm(forms.Form):
    username = forms.CharField(label=(u'Username'),widget = forms.TextInput(attrs = {'placeholder': 'Username'}))
    password = forms.CharField(max_length=16, label=(u'Password'))
