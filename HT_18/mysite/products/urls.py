from django.urls import path
from . import views

urlpatterns = [
    path("", views.search, name="home"),
    path("search/", views.search, name="search"),
    path("cart/", views.cart, name="cart"),
    path("details/<str:product_id>/", views.details, name="details"),
    path("fetch/", views.fetch, name="fetch")
]