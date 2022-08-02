from django.urls import path
from projects.views import (
    show_projects,
    project_details,
    create_project
)

urlpatterns = [
    path("", show_projects, name="list_projects"),
    path("<int:pk>/", project_details, name="show_project"),
    path("create/", create_project, name="create_project")
]
