from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from app_taxi import views

view_main_page = csrf_exempt(views.MainPageView.as_view())

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_main_page)
]
