from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    AbstractUser,
    
)

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique = True, blank=False)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email