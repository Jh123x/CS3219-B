from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index),
    path("todo", views.todo),
    path("todo/<id>", views.update_todo)
]