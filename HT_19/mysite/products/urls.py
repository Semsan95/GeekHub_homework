from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.search, name="search"),
    path("fetch/", views.fetch, name="fetch"),
    path("imported/", views.imported, name="imported"),
    path("<str:product_id>/", views.details, name="details"),
]