from django.db import models
from homework_8.models.validators import validate_future_date
from homework_8.models.statuses import STATUSES


class Task(models.Model):
    title = models.CharField(
        max_length=75
    )
    description = models.TextField()
    categories = models.ManyToManyField('Category', related_name='tasks')
    status = models.CharField(max_length=20, choices=STATUSES, default="New")
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task_manager_task'
        ordering = ('-created_at',)
        verbose_name = 'Task'
        unique_together = ('title', 'created_at')
