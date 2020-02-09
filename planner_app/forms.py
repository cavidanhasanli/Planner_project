from django import forms
from .models import  Task_Model


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task_Model
        fields = [
            'start_place', 'end_place',
            'start_date', 'end_date','task_periods'
        ]
