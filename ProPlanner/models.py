from django.db import models
from django.utils import timezone


class Tasks(models.Model):
    task = models.CharField(max_length=1000)
    due_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.task


task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
