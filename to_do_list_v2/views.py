from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView

from to_do_list_v2.forms.task_form import TaskForm
from to_do_list_v2.models import ToDoListModels


class IndexView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todolists'] = ToDoListModels.objects.all()
        return context


class TaskDetailView(TemplateView):
    template_name = 'detail_task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = get_object_or_404(ToDoListModels, pk=kwargs['pk'])
        return context


class TaskAddView(View):
    def get(self, request):
        context = {
            'form': TaskForm()
        }
        return render(request, 'add_task.html', context)

    def post(self, request):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, "add_task.html", {'form': form})


class TaskEditView(View):
    def get(self, request, pk):
        task = get_object_or_404(ToDoListModels, pk=pk)
        form = TaskForm(instance=task)
        return render(request, 'edit_task.html', {'form': form})

    def post(self, request, pk):
        task = get_object_or_404(ToDoListModels, pk=pk)
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, "edit_task.html", {'form': form})


class TaskDeleteView(View):
    def get(self, request, pk):
        task = get_object_or_404(ToDoListModels, pk=pk)
        return render(request, 'delete_task.html', {'task': task})

    def post(self, request, pk):
        task = get_object_or_404(ToDoListModels, pk=pk)
        if request.POST.get('delete'):
            task.delete()
        return redirect("home")
