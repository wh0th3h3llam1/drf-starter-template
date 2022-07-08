from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from model_utils.models import TimeStampedModel

from core.managers import UserManager


# Create your models here.


class BaseModel(TimeStampedModel):
    """
    An abstract base class model that provides
    `added_on` and `updated_on`
    """

    class Meta:
        abstract = True

    @property
    def added_on(self):
        return self.created

    @property
    def updated_on(self):
        return self.modified

    def save(self, *args, **kwargs):
        if self.pk:
            # If self.pk is not None then it's an update.
            cls = self.__class__
            old = cls.objects.get(pk=self.pk)
            # This will get the current model state since super().save() isn't called yet.
            new = self  # This gets the newly instantiated Mode object with the new values.
            changed_fields = []
            for field in cls._meta.get_fields():
                field_name = field.name
                try:
                    if getattr(old, field_name) != getattr(new, field_name):
                        changed_fields.append(field_name)
                except Exception as ex:  # Catch field does not exist exception
                    pass
            kwargs["update_fields"] = changed_fields
        super().save(*args, **kwargs)


class AbstractUser(AbstractBaseUser):

    username = models.CharField(
        verbose_name=_("Username"),
        max_length=150,
        unique=True,
    )
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    is_staff = models.BooleanField(
        verbose_name=_("Staff Status"),
        default=False,
        help_text="Designate whether the user can log into this admin site.",
    )
    is_superuser = models.BooleanField(
        verbose_name=_("Superuser Status"),
        default=False,
        help_text=_(
            "Designates that this user has all permissions without "
            "explicitly assigning them."
        ),
    )
    is_active = models.BooleanField(
        verbose_name=_("Active"),
        default=True,
        help_text="Designates whether this use should be treated as active. "
        "Unselect this instead of deleting accounts (soft delete)",
    )
    date_joined = models.DateTimeField(
        verbose_name=_("Date Joined"), default=timezone.now
    )

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

    objects = UserManager()

    class Meta:
        abstract = True
