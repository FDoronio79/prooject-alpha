from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from projects.models import (
    Project,
)
from projects.forms import ProjectForm

@login_required
def show_projects(request):
    projects = request.user.projects.all()
    context = {
        "projects": projects,

    }
    return render(request, 'projects/list.html', context)


@login_required
def project_details(request, pk):
    projects = Project.objects.get(pk=pk)
    context = {
        "project": projects
    }
    return render(request, "projects/detail.html", context)


@login_required
def create_project(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        project = form.save()
        return redirect("show_project", pk=project.pk)
    context = {
        "form": form
    }
    return render(request, "projects/create.html", context)
