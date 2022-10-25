from .models import Task
from django.forms import ModelForm, widgets, TextInput


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "theme"]
        widgets = {'title': TextInput(attrs={'class' : 'form-control','placeholder': 'Name'}),
            'task': TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'theme': TextInput(attrs={'class': 'form-control', 'placeholder': 'Theme'}),
        }