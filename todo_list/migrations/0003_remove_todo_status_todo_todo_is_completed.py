# Generated by Django 4.0.4 on 2022-05-23 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0002_alter_todo_deadline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='status_todo',
        ),
        migrations.AddField(
            model_name='todo',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]