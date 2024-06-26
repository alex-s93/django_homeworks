from rest_framework.generics import ListAPIView

from homework_8.models import Task
from homework_8.serializers.tasks import (
    AllTasksSerializer,
    TaskCreateSerializer,
    TaskDetailSerializer
)
from homework_8.views.v2.base_tasks import (
    BaseTaskListCreateView,
    BaseTaskDetailUpdateDeleteView
)


class TaskListCreateView(BaseTaskListCreateView):
    base_model = Task
    serializer_get = AllTasksSerializer
    serializer_post = TaskCreateSerializer


class TaskDetailUpdateDeleteView(BaseTaskDetailUpdateDeleteView):
    base_model = Task
    serializer_get = TaskDetailSerializer
    serializer_put = TaskCreateSerializer


class TaskListByOwnerView(ListAPIView):
    serializer_class = AllTasksSerializer

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
