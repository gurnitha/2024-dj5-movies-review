# config/urls.py
from django.contrib import admin
from django.urls import path, include

from movie import views as movieViews

urlpatterns = [
    # admin 
    path("admin/", admin.site.urls),

    # moview
    path("", include("movie.urls")),
]