from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        superuser = self.create_user(
            email=email,
            password=password,
        )
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True
        superuser.save(using=self._db)
        return superuser


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        max_length=30, unique=True, null=False, blank=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #이름, 학번, 전공, 전화번호, 포지션
    name = models.CharField(default="", null=True, blank=True, max_length=100)
    student_num = models.CharField(
        default="", null=True, blank=True, max_length=100)
    major = models.CharField(default="", null=True, blank=True, max_length=100)
    phone_num = models.CharField(
        default="", null=True, blank=True, max_length=100)
    position = models.CharField(
        default="", null=True, blank=True, max_length=100)

    objects = UserManager()

    USERNAME_FIELD = 'email'
