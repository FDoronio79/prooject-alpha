from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from projects.models import (
    Project,
)
from tasks.models import (
    Task,
)

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
