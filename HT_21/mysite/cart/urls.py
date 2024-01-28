from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("", views.cart_home, name="cart_home"),
    path("clear", views.clear, name="clear"),
    path("<str:product_id>/add/", views.add, name="add"),
    path("<str:product_id>/increase/", views.increase, name="increase"),
    path("<str:product_id>/decrease/", views.decrease, name="decrease"),
    path("<str:product_id>/remove/", views.remove, name="remove"),
]