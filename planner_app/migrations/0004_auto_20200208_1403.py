# Generated by Django 3.0.3 on 2020-02-08 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner_app', '0003_auto_20200208_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_model',
            name='task_periods',
            field=models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly')], max_length=7),
        ),
    ]
