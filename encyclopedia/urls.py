from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new", views.new, name="newpage"),
    path("random", views.random, name="random")
]
