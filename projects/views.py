from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from projects.models import (
    Project,
)

@login_required
def show_projects(request):
    projects = request.user.projects.all()
    context = {
        "projects": projects
    }
    return render(request, 'projects/list.html', context)
