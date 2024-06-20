from django.db.models import Count
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status

from homework_8.models import Category
from homework_8.serializers.categories import CategoryCreateSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer

    @action(detail=False, methods=['get'], url_path='count-tasks')
    def count_tasks(self, request):
        categories_w_tasks_count = Category.objects.annotate(task_count=Count('tasks'))
        data = [
            {
                "name": category.name,
                "task_count": category.task_count
            } for category in categories_w_tasks_count
        ]
        return Response(data=data, status=status.HTTP_200_OK)
