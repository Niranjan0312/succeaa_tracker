# success_tracker/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import TaskCompletionForm
from .models import DailyEvaluation

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('task_list')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'success_tracker/task_list.html', {'tasks': tasks})

def add_task(request):
    # Implement logic to add a new task
    return render(request, 'success_tracker/add_task.html')

def view_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'success_tracker/view_task.html', {'task': task})

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == 'POST':
        form = TaskCompletionForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskCompletionForm(instance=task)

    return render(request, 'success_tracker/complete_task.html', {'form': form, 'task': task})

def home(request):
    return render(request, 'success_tracker/home.html')

def dashboard(request):
    daily_evaluations = DailyEvaluation.objects.all()
    return render(request, 'success_tracker/dashboard.html', {'daily_evaluations': daily_evaluations})