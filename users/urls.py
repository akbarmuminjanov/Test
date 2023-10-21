from django.urls import path
from .views import (login_view, logout_view, signup_view, update_user, profile)


urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup/", signup_view, name="signup"),
    path("update_user/", update_user, name="update_user"),
    path("profile/<int:user_id>", profile, name="profile"),
]