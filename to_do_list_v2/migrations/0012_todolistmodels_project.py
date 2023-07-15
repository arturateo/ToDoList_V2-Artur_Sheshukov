# Generated by Django 4.2.2 on 2023-07-11 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list_v2', '0011_alter_projectmodels_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolistmodels',
            name='project',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, related_name='projects', to='to_do_list_v2.projectmodels', verbose_name='Проекты'),
            preserve_default=False,
        ),
    ]