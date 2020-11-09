
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.


class UserProfileManager(BaseUserManager):

    def create_user(self, email, name, password=None):
        """[summary]

        Args:
            email (str): the new users email address
            name (str): the new users name
            password (str, optional): the new users password. Defaults to None.

        Raises:
            ValueError: notifies the new user that they must enter their email address if none is entered

        Returns:
            user: the user model which contains all the user information and saves it into a database
        """

        if not email:
            raise ValueError("User must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details

        Returns:
            user: the user model which contains all the user information and saves it into a database
        """

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for user in the system

    Args:
        AbstractBaseUser (class): django's built in user model
        PermissionsMixin (class): django's built in permissions model

    Returns:
        str: users name and email address
    """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieves the full name of the user

        Returns:
            str: the full name of the user
        """

        return self.name

    def get_short_name(self):
        """Retrieves the short name of the user

        Returns:
            str: the short name of the user
        """

        return self.name

    def __str__(self):
        """Returns the string representation of our user

        Returns:
            str: string representation of user, i.e. their email
        """
        return self.email
