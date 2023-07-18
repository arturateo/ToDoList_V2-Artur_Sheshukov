from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from to_do_list_v2.forms.task_form import TaskForm
from to_do_list_v2.models import ToDoListModels, ProjectModels


class TaskDetailView(DetailView):
    template_name = 'tasks/detail_task.html'
    queryset = ToDoListModels.objects.all()
    context_object_name = 'data'


class TaskAddView(CreateView):
    template_name = 'tasks/add_task.html'
    form_class = TaskForm

    def form_valid(self, form):
        project = get_object_or_404(ProjectModels, pk=self.kwargs.get("pk"))
        comment = form.save(commit=False)
        comment.project = project
        comment.save()
        form.save_m2m()
        return redirect("to_do_list:project_detail", pk=project.pk)


class TaskEditView(UpdateView):
    model = ToDoListModels
    form_class = TaskForm
    template_name = "tasks/edit_task.html"

    def get_success_url(self):
        print(self.object)
        return reverse("to_do_list:task_detail", kwargs={"pk": self.object.pk})


class TaskDeleteView(DeleteView):
    model = ToDoListModels
    template_name = "tasks/delete_task.html"
    context_object_name = 'tasks'
    success_url = reverse_lazy("to_do_list:home")
