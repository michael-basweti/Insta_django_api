from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        required=True,
        error_messages={
            'required': 'Title is required'
        }
    )
    post = serializers.CharField(
        required=True,
        error_messages={
            'required': 'Body is required'
        }
    )
    author = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Post
        fields = ('id','post','author','title','created_at','updated_at','image_url')

