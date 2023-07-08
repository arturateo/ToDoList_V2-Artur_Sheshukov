from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView, FormView
from django.urls import reverse, reverse_lazy
from to_do_list_v2.forms.task_form import TaskForm
from to_do_list_v2.models import ToDoListModels


class IndexView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todolists'] = ToDoListModels.objects.all().order_by('create_date')
        return context


class TaskDetailView(TemplateView):
    template_name = 'detail_task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = get_object_or_404(ToDoListModels, pk=kwargs['pk'])
        return context


class TaskAddView(FormView):
    success_url = reverse_lazy('home')
    form_class = TaskForm
    template_name = "add_task.html"

    def form_valid(self, form):
        task = form.save()
        return redirect('task_detail', pk=task.pk)


class TaskEditView(FormView):
    success_url = reverse_lazy('home')
    form_class = TaskForm
    template_name = "add_task.html"

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_object(kwargs.get('pk'))
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, pk):
        return get_object_or_404(ToDoListModels, pk=pk)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.task
        return kwargs

    def form_valid(self, form):
        form.save()
        return redirect('task_detail', pk=self.task.pk)


class TaskDeleteView(View):
    def get(self, request, pk):
        task = get_object_or_404(ToDoListModels, pk=pk)
        return render(request, 'delete_task.html', {'task': task})

    def post(self, request, pk):
        task = get_object_or_404(ToDoListModels, pk=pk)
        if request.POST.get('delete'):
            task.delete()
        return redirect("home")
