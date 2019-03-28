from django.urls import path
from .views import PostCreateListView, PostDetail

urlpatterns = [
    path('', PostCreateListView.as_view(), name="post_create_view"),
    path('<int:pk>',PostDetail.as_view(), name="post_detail")
]
