
from django.urls import path
from .views import TaskListView, AddTaskView, DeleteTaskView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('add/', AddTaskView.as_view(), name='add_task'),
    path('delete/<int:task_id>/', DeleteTaskView.as_view(), name='delete_task'),
]
