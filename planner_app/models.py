from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task_Model(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    TASK_PERIOD_CHOICES = [
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly'),
    ]
    task_periods = models.CharField(
        max_length=7,
        choices=TASK_PERIOD_CHOICES
    )
    start_place = models.CharField(max_length=150)
    end_place = models.CharField(max_length=150)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.start_place} | {self.end_place}'