from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from tasks.forms import TaskForm
from tasks.models import Task, Tag


# Create your views here.

class TaskListView(generic.ListView):
    model = Task
    template_name = "tasks/index.html"
    queryset = Task.objects.all().prefetch_related("tags")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"

    def get_success_url(self):
        return reverse_lazy("tasks:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        return reverse_lazy("tasks:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:index")


class ToggleTaskStatusView(generic.View):
    def get(self, request, pk):
        task = Task.objects.get(pk=pk)
        if task.done:
            task.done = False
        else:
            task.done = True
        task.save()
        return redirect(reverse_lazy("tasks:index"))


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "tasks/tag_form.html"
    success_url = reverse_lazy("tasks:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag-list")
