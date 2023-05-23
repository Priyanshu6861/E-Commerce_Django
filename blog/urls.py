from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name="blogHome"),
    path("blogpost/<int:pid>", views.blogpost, name="blogHome")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
