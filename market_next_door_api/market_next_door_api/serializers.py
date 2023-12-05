from rest_framework import serializers
from .models import *

# Customers
class CustomerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Customer
    fields = ['id', 'first_name', 'last_name', 'phone', 'email', 'location']

# Items
class ItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = Item
    fields = ['id', 'item_name', 'vendor', 'price', 'size', 'quantity', 'availability', 'description', 'image']

  def to_representation(self, instance):
    representation = super().to_representation(instance)
    data = {
      "id": representation['id'],
      "type": "item",
      "attributes": {
        "item_name": representation['item_name'],
        "vendor": representation['vendor'],
        "price": representation['price'],
        "size": representation['size'],
        "quantity": representation['quantity'],
        "availability": representation['availability'],
        "description": representation['description'],
        "image": representation['image']
      }
    }
    return data

class VendorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Vendor
    fields = ['id', 'market', 'vendor_name', 'first_name', 'last_name', 'email', 'location']

# preorders
class PreorderSerializer(serializers.ModelSerializer):
  class Meta:
    model = Preorder
    fields = ['id', 'customer', 'vendor', 'item', 'quantity', 'date_created','updated_at','ready']
