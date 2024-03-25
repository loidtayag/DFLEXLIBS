from django.urls import path
from . import views

urlpatterns = [
    path("", views.base, name="base"),
    path("search", views.search, name="search"),
    path("navigate", views.navigate, name="navigate"),
    path("checkValidate", views.checkValidate, name="checkValidate"),
    path("validate", views.validate, name="validate"),
    path("results", views.resultss, name="results"),
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