# Generated by Django 4.2.2 on 2023-07-11 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list_v2', '0007_projectmodels'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectmodels',
            old_name='update_date',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='projectmodels',
            old_name='create_date',
            new_name='start_date',
        ),
    ]
