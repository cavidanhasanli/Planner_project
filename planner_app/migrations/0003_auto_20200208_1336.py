# Generated by Django 3.0.3 on 2020-02-08 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner_app', '0002_task_model_year_in_school'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task_model',
            old_name='year_in_school',
            new_name='task_periods',
        ),
    ]
