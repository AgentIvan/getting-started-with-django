from django.contrib import admin
from django.urls import path

from leads.views import home_page, second_page

app_name = "leads"

urlpatterns = [
    path("", home_page),
    path("all/", second_page),
]
