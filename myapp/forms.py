from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task  # Associate the form with the Task model
        fields = ['title', 'description', 'priority', 'due_date']
        title = forms.CharField(label="Title", max_length=255)
        description = forms.CharField(widget=forms.Textarea)
        priority = forms.ChoiceField(label="Priority", choices=[(
            'low', 'Low'), ('medium', 'Medium'), ('high', 'High')])
        due_date = forms.DateField()