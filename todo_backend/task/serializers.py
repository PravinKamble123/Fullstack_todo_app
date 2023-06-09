from rest_framework import serializers

from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id', 
            'description',
            'status'
        ]


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id', 
            'status',
        ]
        