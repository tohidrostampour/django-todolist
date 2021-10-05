from django.urls import path
from .views import (
    TaskDetail, TaskListCreateView,
    TaskUpdate, TaskDelete, UserLoginView, UserLogoutView)


app_name = 'todolist'
urlpatterns = [
    path('', TaskListCreateView.as_view(), name='tasks'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    # path('', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete')
]
