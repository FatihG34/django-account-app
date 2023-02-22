from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.


class Customer(AbstractUser):
    identity_no = models.CharField(max_length=25, null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photo/%Y/%m/%\d/',
                                      null=True, blank=True, height_field=None, width_field=None, max_length=None)
    address = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True)


class Staff(models.Model):
    staff_user = models.OneToOneField(Customer, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
