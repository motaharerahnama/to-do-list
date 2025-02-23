# tasks/views.py

from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Task

class TaskListView(View):
    def get(self, request):
        tasks = Task.objects.all()
        return render(request, 'tasks/index.html', {'tasks': tasks})

class AddTaskView(View):
    def get(self, request):
        return render(request, 'tasks/add_task.html')
    
    def post(self, request):
        title = request.POST['title']
        Task.objects.create(title=title)
        return redirect(reverse('task_list'))

class DeleteTaskView(View):
    def get(self, request, task_id):
        task = Task.objects.get(id=task_id)
        task.delete()
        return redirect(reverse('task_list'))
