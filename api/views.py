from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializers
# Create your views here.


@api_view(['GET', 'POST'])

def apiOverview(request):
    api_urls={
        'List':'/task-list/',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',
    }
    return Response(api_urls)
@api_view(['GET'])
def tasklist(request):
    task    =   Task.objects.all()
    serializer  =   TaskSerializers(task,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def taskDetail(request,pk):
    task    =   Task.objects.get(id=pk)
    serializer  =   TaskSerializers(task,many=False)
    return Response(serializer.data)
@api_view(['POST'])
def taskCreate(request):
    serializer  =   TaskSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['POST'])
def taskUpdate(request,pk):
    task    =   Task.objects.get(id=pk)
    serializer  =   TaskSerializers(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request,pk):
    task    =   Task.objects.get(id=pk)
    task.delete()
    return Response('Data Deleted')


