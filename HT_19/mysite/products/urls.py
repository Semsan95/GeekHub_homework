from django.urls import path
from . import views

urlpatterns = [
    path("", views.search, name="home"),
    path("search/", views.search, name="search"),
    path("cart/", views.cart, name="cart"),
    path("details/<str:product_id>/", views.details, name="details"),
    path("fetch/", views.fetch, name="fetch"),
    path("imported/", views.imported, name="imported"),
    path("add_to_cart/<str:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("cart_add_button/<str:product_id>/", views.cart_add_button, name="cart_add_button"),
    path("cart_subtract_button/<str:product_id>/", views.cart_subtract_button, name="cart_subtract_button"),
    path("cart_remove_button/<str:product_id>/", views.cart_remove_button, name="cart_remove_button"),
    path("cart_clear_button/", views.cart_clear_button, name="cart_clear_button")
]