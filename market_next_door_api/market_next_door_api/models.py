from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length = 10)
    email = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)