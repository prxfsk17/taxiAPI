from typing import Any

from django.http import HttpRequest
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from app_taxi.models import User

from .forms import RegisterForm


def register(req: HttpRequest) -> Any:
    if req.method == "POST":
        form = RegisterForm(req.POST)
        if form.is_valid():
            form.save()
        return redirect("/taxi/main/")
    else:
        form = RegisterForm()
    return render(req, "registration/register.html", {"form": form})


class MainPageView(ListView):
    model = User


class CreateUserView(CreateView):
    extra_context = {"page_header": "Create user"}
    fields = ("From", "To", "date", "time", "count")
    model = User
    success_url = "/taxi/main/"


class OneUserView(DetailView):
    model = User


class EditMeView(UpdateView):
    extra_context = {"page_header": "Edit user"}
    fields = ("From", "To", "date", "time", "count")
    model = User


class DeleteMeView(DeleteView):
    model = User
    success_url = "/taxi/main/"
