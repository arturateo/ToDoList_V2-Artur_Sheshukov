# Generated by Django 4.2.2 on 2023-07-05 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list_v2', '0002_rename_tasks_todolistmodels_old_tasks'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolistmodels',
            name='tasks',
            field=models.ManyToManyField(related_name='tasks', to='to_do_list_v2.tasksmodel', verbose_name='Типы задач'),
        ),
        migrations.AlterField(
            model_name='todolistmodels',
            name='old_tasks',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='old_tasks', to='to_do_list_v2.tasksmodel', verbose_name='Типы задач'),
        ),
    ]
