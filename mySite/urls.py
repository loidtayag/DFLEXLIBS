from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("upload", views.upload, name="upload"),
    path("filter", views.filter, name="filter"),
    path("results", views.resultss, name="results"),
    path("applications", views.applications, name="applications"),
    path("results/report", views.report, name="report"),
    path("results/info", views.info, name="info"),
    path("results/info/description", views.description, name="description"),
    path("results/info/flow", views.flow, name="flow"),
    path("results/info/performance", views.performance, name="peformance"),
    path("results/info/requirements", views.requirements, name="requirements"),
    path("results/info/configuration", views.configuration, name="configuration"),
    path("results/info/downloadCon", views.downloadCon, name="downloadCon"),
    path("results/info/download", views.download, name="download")
]