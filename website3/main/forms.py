from dataclasses import fields
from .models import Task
from django.forms import ModelForm, widgets, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "theme"]
        widgets = {"title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Name','cols': 10, 'rows': 1 }),
                   "task": Textarea(attrs={'class': 'form-control', 'placeholder': 'Description','cols': 10, 'rows': 5}),
                   "theme": TextInput(attrs={'class': 'form-control', 'placeholder': 'Theme','cols': 10, 'rows': 1}),
                   }
