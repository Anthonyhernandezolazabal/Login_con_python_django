from django.contrib import admin
from django.urls import path,include
from .import views
from app.views import LoginFormViews
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('inicio/',login_required(views.Home),name='home'),
    path('',LoginFormViews.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
]
