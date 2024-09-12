from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.CharField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    district = models.CharField(max_length=50, null=True, blank=True)
    town = models.CharField(max_length=50, null=True, blank=True)
    zip_code = models.CharField(max_length=50, null=True, blank=True)
    phone_number_1 = models.IntegerField(null=True)
    phone_number_2 = models.IntegerField(null=True)
    email = models.EmailField(null=True)
