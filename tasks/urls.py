
from django.contrib import admin
from django.urls import path

from .views import TaskListView, TaskCreateView, TagCreateView

app_name = "tasks"
urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("task/create/", TaskCreateView.as_view(), name="task-create" ),
path("tags/create/", TagCreateView.as_view(), name="tag-create" ),
    ]

