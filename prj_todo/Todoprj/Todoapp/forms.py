from django import forms

from Todoapp.models import Task


class TodoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'priority', 'date']

