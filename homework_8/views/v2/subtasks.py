from homework_8.models import Subtask
from homework_8.serializers.subtasks import (
    SubtaskCreateSerializer,
    SubTaskSerializer
)
from homework_8.views.v2.base_tasks import (
    BaseTaskListCreateView,
    BaseTaskDetailUpdateDeleteView
)


class SubtaskListCreateView(BaseTaskListCreateView):
    base_model = Subtask
    serializer_get = SubTaskSerializer
    serializer_post = SubtaskCreateSerializer


class SubtaskDetailUpdateDeleteView(BaseTaskDetailUpdateDeleteView):
    base_model = Subtask
    serializer_get = SubTaskSerializer
    serializer_put = SubtaskCreateSerializer
