from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from homework_8.models import Subtask

from homework_8.serializers.subtasks import (
    SubTaskSerializer,
    SubtaskCreateSerializer
)


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
