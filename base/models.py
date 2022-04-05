from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    phone = models.BigIntegerField(null=True)
    dob = models.DateField(null=True)

    class Meta:
        app_label = 'base'

    def __str__(self):
        return self.username
