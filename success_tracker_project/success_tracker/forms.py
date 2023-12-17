# success_tracker/forms.py
from django import forms
from .models import Task

class TaskCompletionForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['completed', 'completion_image']
