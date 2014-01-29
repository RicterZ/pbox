from rest_framework import serializers
from pbox_backend.models import Post, Reply, User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply