from django.db import models
from django.contrib.auth.models import  AbstractBaseUser
from django.contrib.auth.models import  PermissionsMixin
from django.contrib.auth.models import  BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """User model manager for user profiles"""

    def create_user(self,name,email,password=None):
        """Create new user profile"""
        if not email:
            raise ValueError('Error is required')

        email = self.normalize_email(email)
        user = self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, name ,email,password):
        """create new super user with given  details"""

        user = self.create_user(name,email,password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using = self._db)

        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for users in the system"""

    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def get_full_name(self):
        """Get full name of user"""
        return self.name

    def  get_short_name(self):
        """Get short name of user"""
        return  self.name

    def __str__(self):
        """Return email of user"""
        return self.name


class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return the model as string"""
        return self.status_text