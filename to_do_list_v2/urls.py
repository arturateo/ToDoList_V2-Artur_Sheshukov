from django.urls import path

from to_do_list_v2.views.errors_views import PageNotFound
from to_do_list_v2.views.projects_views import ProjectList, ProjectAddView, ProjectDetailView, ProjectEditView, \
    ProjectDeleteView
from to_do_list_v2.views.tasks_views import TaskDetailView, TaskAddView, TaskEditView, TaskDeleteView

app_name = 'to_do_list'

urlpatterns = [
    path('page_not_found/', PageNotFound.as_view(), name="page_not_found"),

    path('', ProjectList.as_view(), name="home"),
    path('add_project/', ProjectAddView.as_view(), name="add_project"),
    path('project_detail/<int:pk>/', ProjectDetailView.as_view(), name="project_detail"),
    path('project_edit/<int:pk>/', ProjectEditView.as_view(), name="project_edit"),
    path('project_delete/<int:pk>/', ProjectDeleteView.as_view(), name="delete_project"),

    path('project_detail/<int:pk>/task_add/', TaskAddView.as_view(), name="add_task"),
    path('task_detail/<int:pk>/', TaskDetailView.as_view(), name="task_detail"),
    path('task_edit/<int:pk>/', TaskEditView.as_view(), name="task_edit"),
    path('task_delete/<int:pk>/', TaskDeleteView.as_view(), name="delete_task"),
]
