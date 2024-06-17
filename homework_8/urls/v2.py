from django.urls import path

from homework_8.views.v2.tasks import (
    TaskListCreateView,
    TaskDetailUpdateDeleteView
)
from homework_8.views.v2.subtasks import (
    SubtaskListCreateView,
    SubtaskDetailUpdateDeleteView
)

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view()),
    path('tasks/<int:pk>', TaskDetailUpdateDeleteView.as_view()),
    path('subtasks/', SubtaskListCreateView.as_view()),
    path('subtasks/<int:pk>', SubtaskDetailUpdateDeleteView.as_view())
]
