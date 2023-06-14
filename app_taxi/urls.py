from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from app_taxi import views

view_main_page = views.MainPageView.as_view()
view_create_user = csrf_exempt(views.CreateUserView.as_view())
view_single_user = views.OneUserView.as_view()
view_edit_user = views.EditMeView.as_view()
view_delete_user = views.DeleteMeView.as_view()

urlpatterns = [
    path("main/<int:pk>/edit/", view_edit_user),
    path("main/<int:pk>/delete/", view_delete_user),
    path("main/", view_main_page),
    path("main/<int:pk>/", view_single_user),
    path("user/new/", view_create_user),
]
