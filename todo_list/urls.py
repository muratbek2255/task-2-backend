from django.urls import path

from todo_list.views import TodoListCreateAPIView, TodoRetrieveAPIView


urlpatterns = [
    path('todo/', TodoListCreateAPIView.as_view(), name='todo-url'),
    path('todo/<int:pk>/', TodoRetrieveAPIView.as_view(), name='todo-detail'),

]