from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.http import urlencode
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse, reverse_lazy
from to_do_list_v2.forms.task_form import TaskForm, SearchForm
from to_do_list_v2.models import ToDoListModels


class TasksList(ListView):
    model = ToDoListModels
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'todolists'
    paginate_by = 5
    paginate_orphans = 1
    ordering = ("create_date",)
    page_kwarg = 'page'

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context["form"] = self.form
        if self.search_value:
            context["query"] = urlencode({'search': self.search_value})
            context["search_value"] = self.search_value
        return context

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(Q(summary__icontains=self.search_value) |
                                       Q(description__icontains=self.search_value))
        return queryset


class TaskDetailView(DetailView):
    template_name = 'tasks/detail_task.html'
    queryset = ToDoListModels.objects.all()
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = self.object.tasks.all()
        return context


class TaskAddView(CreateView):
    template_name = 'tasks/add_task.html'
    model = ToDoListModels
    form_class = TaskForm


class TaskEditView(UpdateView):
    success_url = reverse_lazy('home')
    form_class = TaskForm
    template_name = "tasks/add_task.html"

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
        return render(request, 'tasks/delete_task.html', {'task': task})

    def post(self, request, pk):
        task = get_object_or_404(ToDoListModels, pk=pk)
        if request.POST.get('delete'):
            task.delete()
        return redirect("home")
