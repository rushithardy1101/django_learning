from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Tasks
from .serializers import TasksSerializer


@api_view(['GET', 'POST'])
def task_list(request):
    if request.method == 'GET':
        tasks = Tasks.objects.all().order_by('-created_at')
        serializer = TasksSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TasksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):
    try:
        task = Tasks.objects.get(pk=pk)
    except Tasks.DoesNotExist:
        return Response(
            {'error': 'Task not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = TasksSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TasksSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(
            {'message': 'Task deleted successfully'},
            status=status.HTTP_200_OK
        )