from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("upload", views.upload, name="upload"),
    path("results", views.resultss, name="results"),
    path("results/report", views.report, name="report"),
    path("results/info", views.info, name="info")
]