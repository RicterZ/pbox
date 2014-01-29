from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

FORBIDDEN = 0
GENERAL = 1
MANAGER = 2


class Group(models.Model):
    name = models.CharField(max_length=50)
    right = models.IntegerField(default=GENERAL)


class UserExtend(models.Model):
    basic = models.OneToOneField(User)
    group = models.ForeignKey(Group)
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)


class Node(models.Model):
    title = models.CharField(max_length=50)
    intro = models.TextField()


class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    published_date = models.DateTimeField(default=timezone.now())
    node = models.ManyToManyField(Node, blank=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["-id"]


class Reply(models.Model):
    author = models.ForeignKey(User)
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now())
    post = models.ForeignKey(Post)


class Notification(models.Model):
    author = models.ForeignKey(User)
    content = models.TextField()
    send_date = models.DateTimeField(default=timezone.now())