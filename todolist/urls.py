from django.urls import path

from .views import (
    TaskDetail, TaskListCreateView,
    TaskUpdate, TaskDelete)



app_name = 'todolist'
urlpatterns = [
    path('', TaskListCreateView.as_view(), name='tasks'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
]

