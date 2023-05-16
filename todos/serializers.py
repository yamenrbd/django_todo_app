from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers):
    class class Meta:
        model = Todo
        fileds = ("__all__")