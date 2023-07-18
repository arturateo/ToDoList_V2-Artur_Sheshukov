from django.db.models import Q
from django.utils.http import urlencode
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from to_do_list_v2.forms.task_form import SearchForm, ProjectForm
from to_do_list_v2.models import ProjectModels, ToDoListModels


class ProjectList(ListView):
    model = ProjectModels
    template_name = 'projects/projects_list.html'
    context_object_name = 'projects'
    paginate_by = 5
    paginate_orphans = 1
    ordering = ("summary",)
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


class ProjectDetailView(DetailView):
    template_name = 'projects/detail_project.html'
    queryset = ProjectModels.objects.all()
    context_object_name = 'data'

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        tasks = ToDoListModels.objects.all()
        context["form"] = self.form
        if self.search_value:
            context["query"] = urlencode({'search': self.search_value})
            context["search_value"] = self.search_value
            context['tasks'] = tasks.filter(project_id=self.object.pk).filter(Q(summary__icontains=self.search_value) |
                                                                              Q(description__icontains=self.search_value)).distinct()
        else:
            context['tasks'] = tasks.filter(project_id=self.object.pk).filter().distinct()
        return context

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class ProjectAddView(CreateView):
    template_name = 'projects/add_project.html'
    form_class = ProjectForm

    def get_success_url(self):
        return reverse("project_detail", kwargs={"pk": self.object.pk})


class ProjectEditView(UpdateView):
    model = ProjectModels
    form_class = ProjectForm
    template_name = "projects/edit_project.html"

    def get_success_url(self):
        return reverse("project_detail", kwargs={"pk": self.object.pk})


class ProjectDeleteView(DeleteView):
    model = ProjectModels
    template_name = "projects/delete_project.html"
    context_object_name = 'project'
    success_url = reverse_lazy("home")
