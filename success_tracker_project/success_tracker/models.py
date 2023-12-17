# success_tracker/models.py
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    priority = models.IntegerField()
    completed = models.BooleanField(default=False)
    completion_image = models.ImageField(upload_to='completion_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class DailyEvaluation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    marks = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} - {self.date} - Marks: {self.marks}'

