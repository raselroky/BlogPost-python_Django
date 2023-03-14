
from django.contrib import admin
from django.urls import path
from .views import PostsApi,HomeApi

urlpatterns = [
    path('post/',PostsApi.as_view()),
    path('home/',HomeApi.as_view()),
]
