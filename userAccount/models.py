from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    # ? username field will be using for identity number
    # bio = models.TextField(null=True, blank=True) #! biography not necessary for e-commerce
    profile_photo = models.ImageField(upload_to='profile_photo/%Y/%m/%d/', null=True,
                                      help_text="You should save a photo with sizes 500*600", blank=True, height_field=None, width_field=None, max_length=None)
    phone_number_1 = models.CharField(
        max_length=15, help_text="Such as +90 5xx xxx xx xx")
    phone_number_2 = models.CharField(
        max_length=15, help_text="Such as +90 5xx xxx xx xx", null=True, blank=True)
    address_1 = models.CharField(
        max_length=150, help_text="Enter your address")
    address_2 = models.CharField(
        max_length=150, help_text="Enter your address", null=True, blank=True)
    town = models.CharField(
        max_length=25, help_text="Enter your Town that your living")
    city = models.CharField(
        max_length=60, help_text="Enter your City that your living")
    post_code = models.CharField(max_length=20)
    country = models.CharField(
        max_length=60, help_text="Enter your Country that your living")
    updated_date = models.DateTimeField(auto_now=True)
