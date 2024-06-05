from django.db import models
from homework_8.models import Task
from homework_8.models.statuses import STATUSES
from homework_8.models.validators import validate_future_date


class Subtask(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    status = models.CharField(max_length=20, choices=STATUSES, default="New")
    deadline = models.DateTimeField(validators=[validate_future_date])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task_manager_subtask'
        ordering = ('-created_at',)
        verbose_name = 'SubTask'
        unique_together = ('title',)
