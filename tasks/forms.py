from django import forms
from django.template.defaultfilters import title

from tasks.models import Task, Tag


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        required=False,
        widget=(forms.DateTimeInput(
            attrs={'class': "form-control", "type":"datetime-local" })),)
    tags = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, queryset=Tag.objects.all())

    class Meta:
        model = Task
        fields = "__all__"
