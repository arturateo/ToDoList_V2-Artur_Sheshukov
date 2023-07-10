from django.db import models


class TasksModel(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False, verbose_name='Наименование')

    class Meta:
        db_table = 'TasksModel'
        verbose_name = 'Типы задач'
        verbose_name_plural = 'Типы задач'

    def __str__(self):
        return self.title


class StatusModel(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False, verbose_name='Наименование')

    class Meta:
        db_table = 'StatusModel'
        verbose_name = 'Статусы'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.title


class ToDoListModels(models.Model):
    summary = models.CharField(max_length=60, null=False, blank=False, verbose_name='Заголовок')
    description = models.TextField(max_length=300, null=True, blank=True, verbose_name='Название')
    status = models.ForeignKey('to_do_list_v2.StatusModel', related_name='statuses', verbose_name='Статусы',
                               on_delete=models.PROTECT)
    tasks = models.ManyToManyField('to_do_list_v2.TasksModel', related_name='tasks', verbose_name='Типы задач',
                                   blank=False)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        db_table = 'ToDoList'
        verbose_name = 'Список задач'
        verbose_name_plural = 'Список задач'

    def __str__(self):
        return f'{self.summary}'
