# Generated by Django 4.2.2 on 2023-07-05 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list_v2', '0004_auto_20230706_0137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolistmodels',
            name='old_tasks',
        ),
        migrations.AlterField(
            model_name='todolistmodels',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='statuses', to='to_do_list_v2.statusmodel', verbose_name='Статусы'),
        ),
    ]
