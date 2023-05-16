from .models import Todo
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import TodoSerializer

# Create your views here.


class ListTodo(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
