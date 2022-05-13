from django.urls import path

from .views import (
    CategoryListView,
    LeadAssignAgentView,
    LeadCreateView,
    LeadDeleteView,
    LeadDetailView,
    LeadListView,
    LeadUpdateView,
)

app_name = "leads"

urlpatterns = [
    path("", LeadListView.as_view(), name="lead-list"),
    path("<int:pk>/", LeadDetailView.as_view(), name="lead-detail"),
    path("<int:pk>/assign-agent/", LeadAssignAgentView.as_view(), name="lead-assign-agent"),
    path("<int:pk>/delete/", LeadDeleteView.as_view(), name="lead-delete"),
    path("<int:pk>/update/", LeadUpdateView.as_view(), name="lead-update"),
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("create/", LeadCreateView.as_view(), name="lead-create"),
]
