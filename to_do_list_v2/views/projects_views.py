from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from to_do_list_v2.forms.task_form import SearchForm, ProjectForm, ProjectAddAuthorForm
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
            context['tasks'] = tasks.filter(project_id=self.object.pk).distinct()
        return context

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class ProjectAddView(PermissionRequiredMixin, CreateView):
    template_name = 'projects/add_project.html'
    form_class = ProjectForm
    permission_required = 'to_do_list_v2.add_projectmodels'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("to_do_list:page_not_found")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        project = form.save(commit=False)
        project.save()
        project.author.set([self.request.user.id], )
        form.save_m2m()
        return redirect("to_do_list:project_detail", pk=project.pk)

    def get_success_url(self):
        return reverse("to_do_list:project_detail", kwargs={"pk": self.object.pk})

    def has_permission(self):
        return super().has_permission()


class ProjectEditView(PermissionRequiredMixin, UpdateView):
    model = ProjectModels
    form_class = ProjectForm
    template_name = "projects/edit_project.html"
    permission_required = 'to_do_list_v2.change_projectmodels'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("to_do_list:page_not_found")
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("to_do_list:project_detail", kwargs={"pk": self.object.pk})

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().author.all()


class ProjectDeleteView(PermissionRequiredMixin, DeleteView):
    model = ProjectModels
    template_name = "projects/delete_project.html"
    context_object_name = 'project'
    success_url = reverse_lazy("to_do_list:home")
    permission_required = 'to_do_list_v2.delete_projectmodels'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("to_do_list:page_not_found")
        return super().dispatch(request, *args, **kwargs)

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().author.all()


class ProjectAddAuthor(PermissionRequiredMixin, UpdateView):
    model = ProjectModels
    template_name = 'projects/add_project_author.html'
    form_class = ProjectAddAuthorForm
    permission_required = 'to_do_list_v2.change_author_projectmodels'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("to_do_list:page_not_found")
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("to_do_list:project_detail", kwargs={"pk": self.object.pk})

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().author.all()
