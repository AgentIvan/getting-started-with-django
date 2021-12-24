from django.contrib import admin
from django.urls import path

from .views import lead_create, lead_delete, lead_detail, lead_list, lead_update

app_name = "leads"

urlpatterns = [
    path("", lead_list),
    path("<int:pk>/", lead_detail),
    path("<int:pk>/update/", lead_update),
    path("<int:pk>/delete/", lead_delete),
    path("create/", lead_create),
]
