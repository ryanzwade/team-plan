from django.forms import ModelForm, DateInput
from tasks.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["name", "start_date", "due_date", "project", "is_completed", "assignee"]
        widgets = {
            "start_date": DateInput(attrs={"type": "date"}),
            "due_date": DateInput(attrs={"type": "date"}),
        }
