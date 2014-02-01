import re
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from pbox_backend.models import Post, Reply, User, Group, Node, Notification, GENERAL, FORBIDDEN, OWNER, MANAGER


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        read_only_fields = ('published_date',)


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply


class UserSerializer(serializers.ModelSerializer):
    #group = serializers.RelatedField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'group', 'last_login', 'website', 'description')
        read_only_fields = ('last_login',)

    def validate(self, attrs):
        if not re.match(r'^[\w]+$', attrs['username']):
            raise serializers.ValidationError('Username composed only by letters of the alphabet.')
        group_id = attrs['group']
        if group_id is not GENERAL:
            attrs['group'] = Group.objects.filter(right=GENERAL).first()
        if attrs['password']:
            attrs['password'] = make_password(attrs['password'])
        return attrs


class UserDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'group', 'last_login', 'website', 'description')
        read_only_fields = ('last_login', 'email', 'username', 'group')

    def validate(self, attrs):
        if attrs['password']:
            attrs['password'] = make_password(attrs['password'])
        return attrs


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        read_only_fields = ('send_date',)