from django.urls import path

from to_do_list_v2.views import IndexView, TaskDetailView, TaskAddView, TaskEditView, TaskDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('add_task/', TaskAddView.as_view(), name="add_task"),
    path('detail/<int:pk>', TaskDetailView.as_view(), name="task_detail"),
    path('edit/<int:pk>', TaskEditView.as_view(), name="task_edit"),
    path('delete/<int:pk>', TaskDeleteView.as_view(), name="delete_task"),
]
