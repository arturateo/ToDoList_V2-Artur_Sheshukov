# Generated by Django 4.2.2 on 2023-07-24 17:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('to_do_list_v2', '0012_todolistmodels_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmodels',
            name='author',
            field=models.ManyToManyField(related_name='projects', to=settings.AUTH_USER_MODEL, verbose_name='Автор '),
        ),
    ]