from django.urls import path

from homework_8.views.v1.categories import (
    CategoryCreateView,
    CategoryUpdateView
)
from homework_8.views.v1.subtasks import (
    SubTaskListCreateView,
    SubTaskDetailUpdateDeleteView
)
from homework_8.views.v1.tasks import (
    create_task,
    get_tasks,
    get_tasks_stats,
    get_task_by_id,
)

urlpatterns = [
    path('tasks/', create_task),
    path('tasks/all/', get_tasks),
    path('tasks/stats/', get_tasks_stats),
    path('tasks/<int:task_id>', get_task_by_id),
    path('subtasks/', SubTaskListCreateView.as_view()),
    path('subtasks/<int:subtask_id>', SubTaskDetailUpdateDeleteView.as_view()),
    path('categories/', CategoryCreateView.as_view()),
    path('categories/<int:category_id>', CategoryUpdateView.as_view()),
]
