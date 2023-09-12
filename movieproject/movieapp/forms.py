from django import forms
from .models import List


class MovieForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['name','des','year','img']
