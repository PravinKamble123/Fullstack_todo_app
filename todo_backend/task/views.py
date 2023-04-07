from django.shortcuts import render

from .models import Task
from .serializers import TaskSerializer, StatusSerializer

from rest_framework import viewsets 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class TaskViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

@api_view(['GET'])
def get_status(request):
    status = Task.objects.all()
    serializer = StatusSerializer(status, many=True)
    return Response(serializer.data)






