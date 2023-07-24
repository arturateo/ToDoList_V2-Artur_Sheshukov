from django.contrib import admin

from to_do_list_v2.models import TasksModel, StatusModel, ToDoListModels, ProjectModels


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


class ProjectAdminModels(admin.ModelAdmin):
    list_display = ['id', 'summary', 'description', 'start_date', 'end_date']
    list_display_links = ['id', 'summary', 'description']
    search_fields = ['summary', 'description']
    fields = ['summary', 'description', 'author', 'start_date', 'end_date']


admin.site.register(ProjectModels, ProjectAdminModels)


class ToDoListAdminModels(admin.ModelAdmin):
    list_display = ['id', 'summary', 'description', 'create_date', 'update_date']
    list_display_links = ['id', 'summary', 'description']
    list_filter = ['status', 'tasks']
    search_fields = ['summary', 'description']
    readonly_fields = ['create_date', 'update_date']
    filter_horizontal = ('tasks',)
    fields = ['summary', 'description', 'status', 'tasks', 'create_date', 'update_date']

    # def tasks(self):
    #     return self.tasks.title


admin.site.register(ToDoListModels, ToDoListAdminModels)
