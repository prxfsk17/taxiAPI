from django.http import HttpRequest, HttpResponse
from django.views.generic import View, TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView
from django.shortcuts import render
from app_taxi.models import User

# class MainPageView(View):
#     def get(self, request: HttpRequest)->HttpResponse:
#         users: list[User] = list(User.objects.all())
#         return render(
#             request,
#             "app_taxi/user_list.html",
#             {
#                 "users": users
#             }
#         )

class MainPageView(ListView):
    model = User

class CreateUserView(CreateView):
    fields = ("name", "phone")
    model = User
    success_url = "/taxi/main/"

class OneUserView(DetailView):
    model = User

class EditMeView(UpdateView):
    fields = ("name", "phone")
    model = User

