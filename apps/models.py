from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    image = models.ImageField(upload_to='images/', blank=True, null=True)


class Products(models.Model):
    name = models.CharField(max_length=222)


class Category(models.Model):
    name = models.CharField(max_length=222)
