

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .querysets import CustomUserQuerySet

class CustomUser(AbstractUser):
    class UserRoles(models.TextChoices):
        INSTRUCTOR = 'INS', _("Instructor")
        LEARNER = 'LRN', _("Learner")
    email = models.EmailField(
        _("email address"),
        unique=True,
        null=False,
    )
    role = models.CharField(
        _("User Roles"),
        max_length=3,
        choices=UserRoles.choices,
        default=UserRoles.LEARNER
    )
    user_manager = CustomUserQuerySet.as_manager()
    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)



