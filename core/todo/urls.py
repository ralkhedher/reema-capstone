from django.urls import path
from .views import (TaskListView, TaskDetailView, 
                        TaskCreateView, TaskUpdateView, TaskDeleteView)

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", TaskListView.as_view(), name="tasks"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task"),
    path("create/", TaskCreateView.as_view(), name="create-task"),
    path('edit/<int:pk>/', TaskUpdateView.as_view(), name="task-edit"),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name="task-delete"),

]