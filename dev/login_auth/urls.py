from django.urls import path, include
from . import views

urlpatterns = [
        path("login", views.login, name="login"),
        path("signUp", views.signUp, name="signUp"),
        path("logout", views.logout, name="logout"),
        path("dashboard", views.dashboard, name="dashboard"),
 ]
