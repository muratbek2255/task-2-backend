# Generated by Django 4.0.4 on 2022-05-23 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Название')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('deadline', models.DateTimeField(auto_now=True, verbose_name='Дедлайн')),
                ('create_todo', models.DateTimeField(auto_now=True, verbose_name='Создание задачи')),
                ('file', models.FileField(upload_to='')),
                ('status_todo', models.BooleanField(default=True)),
            ],
        ),
    ]