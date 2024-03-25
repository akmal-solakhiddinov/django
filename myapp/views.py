from django.shortcuts import render, redirect,  get_object_or_404
from .models import Task
from .forms import TaskForm

# Create your views here.


def home(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', context={'tasks': tasks})


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'create.html', {'form': form})


def task_update(request, id):
    task = Task.objects.get(pk=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'update.html', {'form': form})


def task_delete(request, id):
    task = get_object_or_404(Task, pk=id)
    if request.method == 'POST':  # Change to POST method
        task.delete()
        # Redirect to a suitable URL after deletion, such as the task list page
        # Change 'task_list' to your actual URL name
        return redirect('home')

    # If the request method is not POST, render the delete confirmation page
    return render(request, 'delete.html', {'task': task})