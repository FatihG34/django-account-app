from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    # ? username field will be using for identity number
    # bio = models.TextField(null=True, blank=True) #! biography not necessary for e-commerce
    profile_photo = models.ImageField(upload_to='profile_photo/%Y/%m/%d/', null=True,
                                      blank=True, height_field=None, width_field=None, max_length=None)
    phone_number_1 = models.CharField(max_length=15)
    phone_number_2 = models.CharField(max_length=15, null=True, blank=True)
    address_1 = models.CharField(max_length=150)
    address_2 = models.CharField(max_length=150, null=True, blank=True)
    town = models.CharField(max_length=25)
    city = models.CharField(max_length=60)
    post_code = models.CharField(max_length=20)
    country = models.CharField(max_length=60)
    updated_date = models.DateTimeField(auto_now=True)
