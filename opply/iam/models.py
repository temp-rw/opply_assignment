from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import CIEmailField, CICharField
from django.db import models

from base.db.models import AbstractBaseModel
from iam.managers import UserManager


class User(AbstractUser, AbstractBaseModel):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField("first name", max_length=50)
    last_name = models.CharField("last name", max_length=50)
    email = CIEmailField(unique=True)
    role = models.ForeignKey(to="iam.Role", on_delete=models.SET_NULL, null=True)

    REQUIRED_FIELDS = ("email",)

    objects = UserManager()

    def __str__(self):
        return f"{self.username} ({self.get_full_name()})"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Role(AbstractBaseModel):
    name = CICharField(max_length=256)

    def __str__(self):
        return f"{self.name}"
