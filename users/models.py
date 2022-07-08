from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel

# Create your models here.


class User(BaseModel, AbstractUser):

    profile_image = models.ImageField(
        verbose_name=_("Profile Picture"),
        upload_to="users/profile_pic/",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
