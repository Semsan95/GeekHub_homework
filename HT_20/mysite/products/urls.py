from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.search, name="search"),
    path("fetch/", views.fetch, name="fetch"),
    path("imported/", views.imported, name="imported"),
    path("<str:product_id>/", views.details, name="details"),
    path("category/<str:category_id>/", views.search, name="category"),
    path("<str:product_id>/edit/", views.edit, name="edit"),
]