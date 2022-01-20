from django.contrib import admin
from django.urls import path,include
from .import views
from app.views import LoginFormViews

urlpatterns = [
    path('', views.Home,name='home'),
    path('login/',LoginFormViews.as_view())
]
