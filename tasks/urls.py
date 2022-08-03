from django.urls import path
from tasks.views import create_task, show_tasks, update_task_status


urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", show_tasks, name="show_my_tasks"),
    path("<int:pk>/complete/", update_task_status, name="complete_task"),
]
