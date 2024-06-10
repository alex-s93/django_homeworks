from rest_framework import serializers

from homework_8.models import Task


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description', 'status', 'deadline')


class AllTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class TasksStatusDeadlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('status', 'deadline')

