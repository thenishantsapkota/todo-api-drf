from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response

from todo_api.models import Todo
from .serializers import TodoSerializer

@api_view(['GET'])
def api_overview(_: HttpRequest) -> Response:
    api_urls = {
        "List": "/task-list/",
        "Detail View": "/task-detail/<str:pk>/",
        "Create": "/task-create/",
        "Update": "/task-update/<str:pk>/",
        "Delete": "/task-delete/<str:pk>/"
    }
    return Response(api_urls)

@api_view(['GET'])
def task_list(_: HttpRequest) -> Response:
    tasks = Todo.objects.all()
    serializer = TodoSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def task_detail(_: HttpRequest, pk: int) -> Response:
    tasks = Todo.objects.get(id=pk)
    serializer = TodoSerializer(tasks, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def task_add(request: HttpRequest):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    

    return Response(serializer.data)

@api_view(['POST'])
def task_update(request: HttpRequest, pk: int) -> Response:
    task = Todo.objects.get(id=pk)
    serializer = TodoSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def task_delete(_: HttpRequest, pk: int) -> Response:
    task = Todo.objects.get(id=pk)
    task.delete()

    return Response(data={"message": f"Todo with ID {pk} deleted successfully!"})