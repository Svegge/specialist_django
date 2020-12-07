from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class RegularUser(AbstractUser):
    phone_number = models.TextField(null=False, blank=False)
    postal_code = models.TextField(null = False, blank=False)
    age = models.PositiveIntegerField(null=True, blank=True)
    sex = models.BooleanField(null=True, blank=True)
