from rest_framework.generics import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q, Count
from django.utils import timezone

from homework_8.models import Task, Subtask, Category
from homework_8.serializers.categories import CategoryCreateSerializer
from homework_8.serializers.subtasks import (
    SubTaskSerializer,
    SubtaskCreateSerializer
)
from homework_8.serializers.tasks import (
    TaskCreateSerializer,
    TasksStatusDeadlineSerializer,
    AllTasksSerializer,
    TaskDetailSerializer
)

# Знаю что подобные вещи надо выносить в отдельный файл констант, но ради одного значения не захотел это делать :)
PER_PAGE = 5


@api_view(['POST', ])
def create_task(request: Request) -> Response:
    """
    Example:
    {
        "title": "new task",
        "description": "new task description",
        "status": "In progress",
        "deadline": "2024-06-11"
    }
    """
    serializer = TaskCreateSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer.save()

    return Response(data=serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', ])
def get_tasks(request: Request) -> Response:
    page = request.query_params.get('page')

    if not page:
        message = {
            "message": "Query parameter 'page' is required."
        }
        return Response(data=message, status=status.HTTP_400_BAD_REQUEST)

    task_status = request.query_params.get('status')
    deadline = request.query_params.get('deadline')

    if task_status and deadline:
        data = [{
            "status": task_status,
            "deadline": deadline
        }]

        status_deadline_serializer = TasksStatusDeadlineSerializer(data=data, many=True)

        if not status_deadline_serializer.is_valid():
            return Response(data=status_deadline_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        tasks = Task.objects.filter(status=task_status, deadline=deadline)

    # TODO: Implement other cases for different search combination.
    #       But according to home-task's description now - it's not required
    else:
        tasks = Task.objects.all()
    paginator = Paginator(tasks, PER_PAGE)

    try:
        page_obj = paginator.page(page)
        page_serializer = AllTasksSerializer(page_obj, many=True)

        response_content = {
            "total_amount": page_obj.paginator.count,
            "per_page": PER_PAGE,
            "values": page_serializer.data
        }
        return Response(data=response_content, status=status.HTTP_200_OK)

    except EmptyPage:
        return Response(data=[], status=status.HTTP_204_NO_CONTENT)

    except PageNotAnInteger as err:
        err_message = {
            "message": f"'{page}' - {str(err)}"
        }
        return Response(data=err_message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
def get_tasks_stats(request: Request) -> Response:
    tasks_amount = Task.objects.all().count()
    status_task_stats = Task.objects.values('status').annotate(count=Count('id'))
    overdue_tasks_amount = Task.objects.filter(~Q(status="Done") & Q(deadline__lt=timezone.now())).count()

    result = {
        "total_amount": tasks_amount,
        "overdue_tasks_amount": overdue_tasks_amount,
        "tasks_stats_by_status": [{stats['status']: stats['count']} for stats in status_task_stats]
    }
    return Response(data=result, status=status.HTTP_200_OK)


@api_view(['GET', ])
def get_task_by_id(request: Request, task_id: int) -> Response:
    task = get_object_or_404(Task, pk=task_id)

    serializer = TaskDetailSerializer(task)

    return Response(data=serializer.data, status=status.HTTP_200_OK)


class CategoryListCreateView(APIView):
    def post(self, request: Request) -> Response:
        serializer = CategoryCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailUpdateDeleteView(APIView):
    def put(self, request, category_id: int) -> Response:
        category = get_object_or_404(Category, pk=category_id)

        serializer = CategoryCreateSerializer(category, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubTaskListCreateView(APIView):
    def get(self, request: Request) -> Response:
        subtasks = Subtask.objects.all()
        if not subtasks.exists():
            return Response(data=[], status=status.HTTP_204_NO_CONTENT)

        serializer = SubTaskSerializer(subtasks, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request):
        serializer = SubtaskCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubTaskDetailUpdateDeleteView(APIView):

    @staticmethod
    def get_subtask(subtask_id: int) -> Subtask:
        return get_object_or_404(Subtask, pk=subtask_id)

    def get(self, request: Request, subtask_id: int) -> Response:
        subtask = self.get_subtask(subtask_id)

        serializer = SubTaskSerializer(subtask)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, subtask_id: int) -> Response:
        subtask = self.get_subtask(subtask_id)

        serializer = SubTaskSerializer(subtask, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, subtask_id: int) -> Response:
        subtask = self.get_subtask(subtask_id)

        subtask.delete()

        delete_msg = {
            "message": f"Subtask with ID[{subtask_id}] was successfully deleted"
        }

        return Response(data=delete_msg, status=status.HTTP_200_OK)
