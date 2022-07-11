# from django.db import models
# from django.contrib.auth.models import AbstractUser


# class CustomUser(AbstractUser):
#     email = models.CharField(max_length=255, unique=True)
#     password = models.CharField(max_length=255)
#     username = models.CharField(max_length=255, blank=True, null=True)
#     is_voter = models.BooleanField(default=False)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ["username"]


from unicodedata import name
# import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
# customUsermanager, customModel


class UserManager(BaseUserManager):
	def create_user(self, email, password=None):
		"""
		Create and return a `User` with an email, username and password.
		"""
		if not email:
			raise ValueError('Users Must Have an email address')
		user = self.model(
			email=self.normalize_email(email),
		)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password):
		"""
		Create and return a `User` with superuser (admin) permissions.
		"""
		if password is None:
			raise TypeError('Superusers must have a password.')
		user = self.create_user(email, password)
		user.is_superuser = True
		user.is_staff = True
		user.save()
		return user

	def create_voteruser(self, email, password):
		if password is None:
			raise TypeError('Voter must have a password')
		user = self.create_user(email, password)
		user.is_voter = True
		user.save()
		return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
    	verbose_name='email address', max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_voter = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'    # username field is email
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email

















