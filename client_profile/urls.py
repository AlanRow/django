from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("account", views.account, name="account"),
    path("register", views.register, name="register"),
]
