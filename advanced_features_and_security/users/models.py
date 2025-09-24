from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()

    class Meta:
        permissions = [
            ("can_view", "Can view user"),
            ("can_create", "Can create user"),
            ("can_edit", "Can edit user"),
            ("can_delete", "Can delete user"),
        ]

    def __str__(self):
        return self.username
