from django import forms
from django.forms import widgets

from to_do_list_v2.models import ToDoListModels


class TaskForm(forms.ModelForm):
    class Meta:
        model = ToDoListModels
        fields = ['summary', 'description', 'status', 'tasks']
        widgets = {'summary': widgets.TextInput(attrs={'class': 'form-control'}),
                   'description': widgets.Textarea(attrs={'class': 'form-control'}),
                   'status': widgets.Select(attrs={'class': 'form-control'}),
                   'tasks': widgets.CheckboxSelectMultiple
                   }
