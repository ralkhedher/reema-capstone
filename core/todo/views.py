from urllib import request
from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, DeleteView, UpdateView, FormView

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login




from .models import Task



class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    template_name = 'task_form.html'
    success_url = reverse_lazy('tasks')

    # def form_valid(self, form):
    #     form.instance.user = self.user
    #     return super(TaskCreateView).form_valid(form)

class TaskListView(ListView):
    model = Task 
    template_name = 'tasks.html'
    context_object_name = "tasks" #-> overide the default object_list

    # rwtric user to viw only tasks they create
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['tasks'] = context['tasks'].filter(user=self.request.user)
    #     return context


class TaskDetailView(DetailView):
    model =  Task
    template_name = 'task_detail.html'
    context_object_name = 'task' 

class TaskUpdateView(UpdateView):
    model = Task 
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')
    context_object_name = "task"
    template_name = "update_task.html"

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("tasks")
    context_object_name = "task"
    template_name = "delete_task.html"



