from django.urls import path
from projects.views import (
    show_projects,
    project_details
)

urlpatterns = [
    path("", show_projects, name="list_projects"),
    path("<int:pk>/", project_details, name="show_project"),
]
