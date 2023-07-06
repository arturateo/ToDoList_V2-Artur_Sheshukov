from django import forms
from django.forms import widgets

from to_do_list_v2.models import ToDoListModels, StatusModel, TasksModel


class TaskForm(forms.ModelForm):
    status = forms.ModelChoiceField(required=True, queryset=StatusModel.objects.all(), widget=widgets.Select(
        attrs={'class': 'form-control'}))
    tasks = forms.ModelMultipleChoiceField(required=True, queryset=TasksModel.objects.all(),
                                           widget=widgets.CheckboxSelectMultiple())

    class Meta:
        model = ToDoListModels
        fields = ['summary', 'description', 'status', 'tasks']
        widgets = {'summary': widgets.TextInput(attrs={'class': 'form-control'}),
                   'description': widgets.Textarea(attrs={'class': 'form-control'}),
                   }
