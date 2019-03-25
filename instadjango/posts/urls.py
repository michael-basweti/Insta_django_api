from django.urls import path
from .views import PostCreateListView

urlpatterns = [
    path('', PostCreateListView.as_view(), name="post_create_view"),
]
