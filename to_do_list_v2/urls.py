from django.urls import path

from to_do_list_v2.views.projects_views import ProjectList, ProjectAddView, ProjectDetailView, ProjectEditView, \
    ProjectDeleteView
from to_do_list_v2.views.tasks_views import TasksList, TaskDetailView, TaskAddView, TaskEditView, TaskDeleteView

urlpatterns = [
    path('', ProjectList.as_view(), name="home"),
    path('add_project/', ProjectAddView.as_view(), name="add_project"),
    path('project_detail/<int:pk>', ProjectDetailView.as_view(), name="project_detail"),
    path('project_edit/<int:pk>', ProjectEditView.as_view(), name="project_edit"),
    path('project_delete/<int:pk>', ProjectDeleteView.as_view(), name="delete_project"),

    # path('add_task/', TaskAddView.as_view(), name="add_task"),
    # path('project_detail/<int:pk>/detail/<int:pk>', TaskDetailView.as_view(), name="task_detail"),
    # path('edit/<int:pk>', TaskEditView.as_view(), name="task_edit"),
    # path('delete/<int:pk>', TaskDeleteView.as_view(), name="delete_task"),
]
