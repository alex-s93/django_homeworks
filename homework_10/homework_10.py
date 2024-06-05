import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.utils import timezone
from datetime import timedelta
from homework_8.models import Task, Subtask
from django.db.models import Q, F


def main():
    # 1. Создание записей:

    # Task:
    # - title: "Prepare presentation".
    # - description: "Prepare materials and slides for the presentation".
    # - status: "New".
    # - deadline: Today's date + 3 days.
    Task.objects.create(
        title='Prepare presentation',
        description='Prepare materials and slides for the presentation',
        status='New',
        deadline=timezone.now() + timedelta(days=3)
    )

    # SubTasks для "Prepare presentation":
    # - title: "Gather information".
    # - description: "Find necessary information for the presentation".
    # - status: "New".
    # - deadline: Today's date + 2 days.
    # --------------------------------------------
    # - title: "Create slides".
    # - description: "Create presentation slides".
    # - status: "New".
    # - deadline: Today's date + 1 day.
    main_task = Task.objects.get(title='Prepare presentation')

    subtasks = [
        Subtask(
            title='Gather information',
            description='Find necessary information for the presentation',
            status='New',
            deadline=timezone.now() + timedelta(days=2),
            task=main_task
        ),
        Subtask(
            title='Create slides',
            description='Create presentation slides',
            status='New',
            deadline=timezone.now() + timedelta(days=1),
            task=main_task
        ),
    ]

    Subtask.objects.bulk_create(subtasks)

    # 2. Чтение записей:

    # Tasks со статусом "New":
    # - Вывести все задачи, у которых статус "New".
    new_tasks = Task.objects.filter(status="New")
    print(list(new_tasks))

    # SubTasks с просроченным статусом "Done":
    # - Вывести все подзадачи, у которых статус "Done", но срок выполнения истек.
    expired_completed_subtasks = Subtask.objects.filter(Q(status="Done") & Q(deadline__lt=timezone.now()))
    print(list(expired_completed_subtasks))

    # 3. Изменение записей:
    # - Измените статус "Prepare presentation" на "In progress".
    task_1 = Task.objects.get(title="Prepare presentation")
    task_1.status = "In progress"
    task_1.save()

    # - Измените срок выполнения для "Gather information" на два дня назад.
    Subtask.objects.filter(title="Gather information").update(deadline=F('deadline') - timedelta(days=2))

    # - Измените описание для "Create slides" на "Create and format presentation slides".
    # Option 1
    Subtask.objects.filter(title__exact='Create slides').update(title="Create and format presentation slides")
    # Option 2
    subtask_2 = Subtask.objects.get(title__exact='Create slides')
    subtask_2.title = "Create and format presentation slides"
    subtask_2.save()

    # 4. Удаление записей:
    # - Удалите задачу "Prepare presentation" и все ее подзадачи.
    Task.objects.get(title="Prepare presentation").delete()

if __name__ == '__main__':
    main()
