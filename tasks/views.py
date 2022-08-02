from sqlite3 import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tasks.forms import TaskForm
from tasks.models import Task


@login_required
def create_task(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        task = form.save()
        return redirect("show_project", pk=task.project.pk)
    context = {
        "form": form
    }
    return render(request, "tasks/create.html", context)


@login_required
def show_tasks(request):
    tasks = Task.objects.filter(assignee=request.user)
    context = {
        "tasks": tasks
    }
    return render(request, "tasks/list.html", context)


def update_task_status(request, pk):
    is_completed = request.POST.get('is_completed')
    task = Task.objects.get(pk=pk)
    try:
        task.is_completed = is_completed
        task.save()
    except IntegrityError:
        pass
    return redirect("show_my_tasks")
