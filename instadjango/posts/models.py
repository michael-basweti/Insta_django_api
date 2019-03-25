from django.db import models
from authentication.models import MyUser

class Post(models.Model):
    author = models.ForeignKey(MyUser, related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    post = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title
