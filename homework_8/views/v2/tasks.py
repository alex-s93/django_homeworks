from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView, get_object_or_404
)
from rest_framework.response import Response
from rest_framework import status

from homework_8.models import Task
from homework_8.serializers.tasks import (
    AllTasksSerializer,
    TaskCreateSerializer,
    TaskDetailSerializer
)


class TaskPaginator(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 5


class TaskListCreateView(ListCreateAPIView):
    queryset = Task.objects.all()
    pagination_class = TaskPaginator

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AllTasksSerializer

        else:
            return TaskCreateSerializer


class TaskDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()

    def get_object(self):
        return get_object_or_404(Task, pk=self.kwargs['pk'])

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return TaskCreateSerializer
        else:
            return TaskDetailSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        # NOTE: на этом моменте вызывается именно сериализатор TaskCreateSerializer - проверено
        #       в классе BaseSerializer в момент вызова метода id_valid в переменной self.fields
        #       присутствует поле created_at типа HiddenField(default=CreateOnlyDefault(<function now>))
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
