from django.contrib import admin
from django.urls import path,include
from .import views
from app.views import LoginFormViews

urlpatterns = [
    path('inicio/', views.Home,name='home'),
    path('',LoginFormViews.as_view())
]
