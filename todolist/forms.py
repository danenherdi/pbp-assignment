from django import forms
from .models import Task

class InputTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']