from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
]
