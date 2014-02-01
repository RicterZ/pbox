from django.utils import timezone
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import status
from permissions import IsAuthorOrReadOnly
from serializers import PostSerializer, UserSerializer, GroupSerializer, NodeSerializer, \
    UserDataSerializer, NotificationSerializer, ReplySerializer
from pbox_backend.models import Post, User, Group, Node, Notification


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    #serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    #permission_classes = (AllowAny,)

    def get_serializer_class(self):
        print self.action
        return PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    #serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    #permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.action in [u'update', u'partial_update']:
            return UserDataSerializer
        else:
            return UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (AllowAny,)


class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    permission_classes = (AllowAny,)


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = (AllowAny,)