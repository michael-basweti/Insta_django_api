from django.urls import path
from .views import UserCreateView, LoginApiView

urlpatterns = [
    path('users/', UserCreateView.as_view(), name="user_create_view"),
    path("login/", LoginApiView.as_view(), name="login"),
]
