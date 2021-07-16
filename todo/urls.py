from django.urls import path, include
from .views import TodoCreateAPIView,   TodoDetailAPIView, TodoListAPIView
app_name='todo'

urlpatterns = [
    path('', TodoListAPIView.as_view(), name='list'),
    path('create/', TodoCreateAPIView.as_view(), name='create'),
    path('<int:id>/', TodoDetailAPIView.as_view(), name='detail'),
]
