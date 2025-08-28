from django.db import models

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

class User(AbstractUser):
    yosh = models.FloatField(validators=[MinValueValidator(0.0)])
    ish_vaqti = models.CharField(max_length=100)

    def __str__(self):
        return self.username