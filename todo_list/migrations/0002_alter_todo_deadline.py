# Generated by Django 4.0.4 on 2022-05-23 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.DateTimeField(verbose_name='Дедлайн'),
        ),
    ]
