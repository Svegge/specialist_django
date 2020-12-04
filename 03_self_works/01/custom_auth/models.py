from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    phone_number = models.TextField(null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    salary_amount = models.FloatField(null=True, blank=True)
    