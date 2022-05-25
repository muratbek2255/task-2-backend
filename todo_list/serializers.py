from rest_framework import serializers

from todo_list.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title', 'comment', 'deadline', 'create_todo', 'file', 'status_todo', 'user')
