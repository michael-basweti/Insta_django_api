from django.urls import path
from .views import UserCreateView, LoginApiView, ProfileView

urlpatterns = [
    path('users/', UserCreateView.as_view(), name="user_create_view"),
    path("login/", LoginApiView.as_view(), name="login"),
    # path('profiles/',ProfileListAPIView.as_view(), name='view_all'),
    path('profiles/<int:user_id>/', ProfileView.as_view(), name='user-profile'),
]
