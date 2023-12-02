from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Customer
    fields = ['first_name', 'last_name', 'phone', 'email', 'location']