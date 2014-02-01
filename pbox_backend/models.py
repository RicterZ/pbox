from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager


FORBIDDEN = 4
GENERAL = 3
MANAGER = 2
OWNER = 1


class PboxUserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_superuser, is_staff, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, is_superuser=is_superuser,
                          is_active=True, last_login=now, is_staff=is_staff,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, True, True, **extra_fields)


class Group(models.Model):
    name = models.CharField(max_length=50, unique=True)
    right = models.IntegerField()

    def __unicode__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField('username', max_length=30, unique=True)
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=True)
    date_joined = models.DateTimeField('date joined', default=timezone.now)
    email = models.EmailField(max_length=200, unique=True)
    group = models.ForeignKey(Group, default=GENERAL)
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)
    #is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    objects = PboxUserManager()

    def __unicode__(self):
        return self.username

    def get_username(self):
        return self.username

    def get_short_name(self):
        return self.username


class Node(models.Model):
    title = models.CharField(max_length=50, unique=True)
    intro = models.TextField()

    def __unicode__(self):
        return self.title


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
    post = models.ForeignKey(Post, related_name='reply')

    class Meta:
        ordering = ["-id"]


class Notification(models.Model):
    author = models.ForeignKey(User, related_name='send_notifications')
    receiver = models.ForeignKey(User, related_name='notifications')
    content = models.TextField()
    send_date = models.DateTimeField(default=timezone.now())

