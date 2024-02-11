from django.urls import path
from django.contrib.auth import views
from . import views as accounts_views


app_name = 'accounts'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'), 
    path('logout/', views.LogoutView.as_view(next_page='products:search'), name='logout'),
    path('profile/', accounts_views.profile, name='profile'),
]