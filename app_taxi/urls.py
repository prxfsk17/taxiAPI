from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from app_taxi import api
from app_taxi import views

api_view_main_page = csrf_exempt(api.MainPageView.as_view())
view_main_page = views.MainPageView.as_view()
view_create_user =  csrf_exempt(views.CreateUserView.as_view())
view_single_user = views.OneUserView.as_view()
view_edit_user = views.EditMeView.as_view()

urlpatterns = [


    path('main/<int:pk>/edit/', view_edit_user),
    path('main/', view_main_page),
    path('main/<int:pk>/', view_single_user),
    path('user/new/', view_create_user),




    path('api/', api_view_main_page),
    path('api/<int:user_id>/', api_view_main_page)
]
