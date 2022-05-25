from django.http import HttpResponse, Http404
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from todo_list.models import Todo
from todo_list.serializers import TodoSerializer


class TodoListCreateAPIView(APIView):

    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['is_completed']
    search_fields = ['title', 'user']
    ordering_fields = ['is_completed', 'user']

    def get(self, request):
        todo_qs = Todo.objects.select_related('users').all()
        todo_srz = TodoSerializer(todo_qs, many=True)
        return Response(todo_srz.data, status=status.HTTP_200_OK)

    def post(self, request):
        body = request.data
        todo_qs = Todo.objects.create(
            title=body['title'], comment=body['comment'],
            deadline=body['deadline'], create_todo=body['create_todo'],
            file=body['file'], status_todo=body['status_todo'],
            user=body['user'],
        )
        todo_srz = TodoSerializer(todo_qs, many=False)
        return Response(todo_srz.data, status=status.HTTP_201_CREATED)


class TodoRetrieveAPIView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        try:
            todo = Todo.objects.get(id=pk)
        except Todo.DoesNotExits:
            return Response({'message': 'Todo not found.'}, status=status.HTTP_404_NOT_FOUND)
        todo_srz = TodoSerializer(todo, many=False)
        return Response(todo_srz.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            todo = Todo.objects.get(id=pk)
        except Todo.DoesNotExits:
            return Response({'message': 'Todo not found.'}, status=status.HTTP_404_NOT_FOUND)
        todo.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        body = request.data
        try:
            todo = Todo.objects.get(id=pk)
        except Todo.DoesNotExits:
            raise Http404
        if not permissions.IsAuthenticated:
            return Response(status=status.HTTP_403_FORBIDDEN)
        todo.title = body['title']
        todo.comment = body['comment']
        todo.deadline = body['deadline']
        todo.create_todo = body['create_todo']
        todo.file = body['file']
        todo.status_todo = body['status_todo']
        todo.user = body['user']
        todo.save()

        todo_srz = TodoSerializer(todo, many=False)
        return Response(todo_srz.data, status=status.HTTP_200_OK)
