from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tasks.forms import TaskForm


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
