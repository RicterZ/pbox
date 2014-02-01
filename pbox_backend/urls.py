from rest_framework import routers
from django.conf.urls import patterns, url, include
from pbox_backend import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', views.UserViewSet, base_name='user')
router.register(r'posts', views.PostViewSet, base_name='post')
router.register(r'notification', views.NotificationViewSet, base_name='notification')
router.register(r'manage/groups', views.GroupViewSet, base_name='group')
router.register(r'manage/nodes', views.NodeViewSet, base_name='node')


urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       )
