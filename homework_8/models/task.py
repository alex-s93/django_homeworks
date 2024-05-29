from django.db import models
from homework_8.models.validators import validate_future_date

CATEGORIES = [
    ("New", "New"),
    ("In progress", "In progress"),
    ("Pending", "Pending"),
    ("Blocked", "Blocked"),
    ("Done", "Done")
]


class Task(models.Model):
    title = models.CharField(
        max_length=75,
        unique_for_date='created_at'
    )
    description = models.TextField()
    categories = models.ManyToManyField('Category')
    status = models.CharField(max_length=20, choices=CATEGORIES, default="New")
    deadline = models.DateTimeField(validators=[validate_future_date])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
