from django.contrib import admin

from todo_list.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass
