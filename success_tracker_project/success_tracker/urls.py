# success_tracker/urls.py
from django.urls import path
from .views import task_list, add_task, view_task, complete_task
from .views import task_list, complete_task, register
urlpatterns = [
    path('tasks/', task_list, name='task_list'),
    path('tasks/add/', add_task, name='add_task'),
    path('tasks/<int:task_id>/', view_task, name='view_task'),
    path('tasks/<int:task_id>/complete/', complete_task, name='complete_task'),
    path('register/', register, name='register'),  # Add this line for registration
    path('tasks/<int:task_id>/complete/', complete_task, name='complete_task'),
]
