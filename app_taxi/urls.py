from django.contrib import admin
from django.urls import path
from app_taxi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.handle_main_page)
]
