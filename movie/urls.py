# movie/urls.py
from django.urls import path

from movie import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("about/", views.about_view, name="about"),
]