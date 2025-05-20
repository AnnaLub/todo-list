
from django.contrib import admin
from django.urls import path

from .views import (TaskListView,
                    TaskCreateView,
                    TagCreateView,
                    TaskUpdateView,
                    TaskDeleteView,
                    ToggleTaskStatusView,
                    )

app_name = "tasks"
urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/toggle-task-status/", ToggleTaskStatusView.as_view(), name="toggle-task-status"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create" ),
    ]
