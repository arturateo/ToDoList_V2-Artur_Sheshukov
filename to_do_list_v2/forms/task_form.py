from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from to_do_list_v2.models import ToDoListModels, ProjectModels


class TaskForm(forms.ModelForm):
    class Meta:
        model = ToDoListModels
        fields = ['summary', 'description', 'status', 'tasks']
        widgets = {'summary': widgets.TextInput(attrs={'class': 'form-control'}),
                   'description': widgets.Textarea(attrs={'class': 'form-control'}),
                   'status': widgets.Select(attrs={'class': 'form-control'}),
                   'tasks': widgets.CheckboxSelectMultiple
                   }

    def clean_summary(self):
        summary = self.cleaned_data['summary']
        if len(summary) < 10:
            raise ValidationError('This field should be at least %(length)d symbols long!', code='too_short_summary',
                                  params={'length': 10})
        return summary

    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) < 20:
            raise ValidationError('This field should be at least %(length)d symbols long!',
                                  code='too_short_description',
                                  params={'length': 20})
        return description


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")


class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectModels
        fields = ['summary', 'description', 'start_date', 'end_date']
        widgets = {'summary': widgets.TextInput(attrs={'class': 'form-control'}),
                   'description': widgets.Textarea(attrs={'class': 'form-control'}),
                   'start_date': widgets.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'type': 'date'}),
                   'end_date': widgets.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'type': 'date'})}


class ProjectAddAuthorForm(forms.ModelForm):
    class Meta:
        model = ProjectModels
        fields = ['author']
        widgets = {'author': widgets.SelectMultiple(attrs={'class': 'form-control'})}