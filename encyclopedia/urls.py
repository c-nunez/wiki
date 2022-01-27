from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new", views.new, name="newpage"),
    path("search", views.search, name="search"),
    path("wiki/<str:entry>", views.entry, name="entry")
]
