from rest_framework import serializers
from django.utils import timezone

from homework_8.models import Task
from homework_8.serializers.subtasks import SubTaskSerializer


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description', 'status', 'deadline')

    def validate_deadline(self, value):
        if value <= timezone.now():
            raise serializers.ValidationError('Deadline must be in the future')
        return value


class AllTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class TasksStatusDeadlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('status', 'deadline')


class TaskDetailSerializer(serializers.ModelSerializer):
    subtasks = SubTaskSerializer(many=True)

    class Meta:
        model = Task
        fields = '__all__'
