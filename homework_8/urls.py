from django.urls import path
from homework_8.views import create_task, get_tasks, get_tasks_stats


urlpatterns = [
    path('', create_task),
    path('all/', get_tasks),
    path('stats/', get_tasks_stats)
]
