from signal import raise_signal
from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from todo_api.models import Todo
from .serializers import TodoSerializer


class TodoView(APIView):
    
    def get(self, request: HttpRequest, *args, **kwargs):
        tasks = Todo.objects.all()
        serializer = TodoSerializer(tasks, many=True)
        return Response(serializer.data)
    
    def post(self, request: HttpRequest, *args, **kwargs):
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
    
    def put(self, request: HttpRequest, pk:int, *args, **kwargs):
        task = Todo.objects.get(id=pk)
        serializer = TodoSerializer(instance=task, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data)
    
    def delete(self, request: HttpRequest, pk: int, *args, **kwargs):
        task = Todo.objects.get(id=pk)
        task.delete()

        return Response(data={"message": f"Todo with ID {pk} deleted successfully!"})

    

@api_view(['GET'])
def task_detail(_: HttpRequest, pk: int) -> Response:
    tasks = Todo.objects.get(id=pk)
    serializer = TodoSerializer(tasks, many=False)
    return Response(serializer.data)
    