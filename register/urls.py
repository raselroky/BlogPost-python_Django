
from django.contrib import admin
from django.urls import path
from .views import RegisterApi,LoginApi

urlpatterns = [
    path('registerapi/',RegisterApi.as_view()),
    path('loginapi/',LoginApi.as_view()),
]
