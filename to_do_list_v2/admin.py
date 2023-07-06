from django.contrib import admin

from to_do_list_v2.models import TasksModel, StatusModel, ToDoListModels


class TasksAdminModels(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    fields = ['title']


admin.site.register(TasksModel, TasksAdminModels)


class StatusAdminModels(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    fields = ['title']


admin.site.register(StatusModel, StatusAdminModels)


class ToDoListAdminModels(admin.ModelAdmin):
    list_display = ['id', 'summary', 'description', 'status', 'tasks', 'create_date', 'update_date']
    list_display_links = ['id', 'summary', 'description', 'status', 'tasks']
    list_filter = ['summary', 'description', 'status', 'tasks']
    search_fields = ['summary', 'description', 'status', 'tasks']
    readonly_fields = ['create_date', 'update_date']
    fields = ['summary', 'description', 'status', 'tasks', 'create_date', 'update_date']

    def tasks(self):
        return self.tasks.title

admin.site.register(ToDoListModels, ToDoListAdminModels)
