from re import M
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

MAX_LENGTH = 255


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Create user by username and password"""
        if not email:
            raise ValueError('User must have an email!')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password):
        """Create superuser by username and password"""
        user = self.create_user(email=email, password=password)
        user.is_superuser = True
        user.save(using=self.db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User model"""
    USERNAME_FIELD = 'email'
    username = None
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    last_login_ip = models.CharField(
        max_length=45, blank=True, null=True)  # 45 is the longest ip address characters
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    @property
    def is_staff(self):
        return self.is_superuser

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"{self.email!r}"
