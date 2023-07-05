from django.db import models

TASKS = [('Task', 'Задача'), ('Bug', 'Ошибка'), ('Enhancement', 'Улучшение')]
STATUS = [('New', 'Новый'), ('In Progress', 'В процессе'), ('Done', 'Выполнено')]


class TasksModel(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False, verbose_name='Наименование', choices=TASKS)


class StatusModel(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False, verbose_name='Наименование', choices=STATUS)


class ToDoListModels(models.Model):
    summary = models.CharField(max_length=60, null=False, blank=False, verbose_name='Заголовок')
    description = models.TextField (max_length=300, null=True, blank=True, verbose_name='Название')
    status = models.ForeignKey('to_do_list_v2.StatusModel', related_name='statuses', verbose_name='Статусы',
                               on_delete=models.CASCADE)
    task = models.ForeignKey('to_do_list_v2.StatusModel', related_name='tasks', verbose_name='Типы задач',
                             on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
