from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import serializers, status


class TodoCreateAPIView(CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    
class TodoListAPIView(ListAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    

class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    lookup_field = 'id'
    
    def retrieve(self, request, id=None):
        try:                                                        # try to get the todo
            todo = Todo.objects.get(id=id)
        except Todo.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)   # if not found, return 404
        
        serializer = TodoSerializer(todo)                     # serialize the todo
        return Response(serializer.data)                            # return the serialized todo
    
    
    def put(self, request, id=None):
        try:                                                        # try to get the todo
            todo = Todo.objects.get(id=id)
        except Todo.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        
        serializer = TodoSerializer(todo, data=request.data)  # convert complex data by passing into serializer 
        
        if serializer.is_valid():                                   # check for validation of data
            serializer.save()
            return Response(serializer.data)                        # return updated the JSON response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # return error for invalid data


    def delete(self, request, id=None):
        try:
            todo = Todo.objects.get(id=id)
        except Todo.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)  # return 404 if not found
        
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)         # return 204 if deleted
         
    
    