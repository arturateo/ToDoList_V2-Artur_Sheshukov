from django.urls import path

from to_do_list_v2.views.tasks_views import TasksList, TaskDetailView, TaskAddView, TaskEditView, TaskDeleteView

urlpatterns = [
    path('', TasksList.as_view(), name="home"),
    path('add_task/', TaskAddView.as_view(), name="add_task"),
    path('detail/<int:pk>', TaskDetailView.as_view(), name="task_detail"),
    path('edit/<int:pk>', TaskEditView.as_view(), name="task_edit"),
    path('delete/<int:pk>', TaskDeleteView.as_view(), name="delete_task"),
]
