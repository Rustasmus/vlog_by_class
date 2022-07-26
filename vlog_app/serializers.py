from rest_framework import serializers
from .models import *


class PostSerializers(serializers.ModelSerializer):
    img = serializers.ImageField(required=False, max_length=None, allow_empty_file=True, use_url=True)
    class Meta:
        model = Post
        fields = ('id', 'title', 'img', 'description', 'update_date', 'user_id')
        # exclude = ()


class MyProfilePostSerializers(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'img', 'description', 'is_draft', 'update_date')


class CreatePostSerializers(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'img', 'description', 'is_draft')


class PostUpdateSerializers(serializers.ModelSerializer):

    title = serializers.CharField(required=True)
    img = serializers.ImageField(required=False, max_length=None, allow_empty_file=True, use_url=True)
    description = serializers.CharField(required=True)
    is_delete = serializers.BooleanField(required=True)
    is_draft = serializers.BooleanField(required=True)

    class Meta:
        model = Post
        fields = ('title', 'img', 'description', 'is_draft', 'is_delete')


class PostDetailSerializers(serializers.ModelSerializer):
    img = serializers.ImageField(required=False, max_length=None, allow_empty_file=True, use_url=True)
    class Meta:
        model = Post
        fields = ('title', 'img', 'description', 'create_date', 'update_date', 'user_id')
        
