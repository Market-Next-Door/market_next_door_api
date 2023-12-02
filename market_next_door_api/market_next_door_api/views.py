from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
import pdb

# Customer CRUD functions
@api_view(['GET', 'POST']) 
def customer_list(request):

  if request.method == 'GET':
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)
  
  elif request.method == 'POST':
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def customer_details(request, id):

  try:
    customer = Customer.objects.get(pk=id)
  except Customer.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    serializer = CustomerSerializer(customer)
    return Response(serializer.data)
  
  elif request.method == 'PUT':
    customer_data = CustomerSerializer(customer, data=request.data)
    if customer_data.is_valid():
      customer_data.save()
      return Response(customer_data.data)
    return Response(customer_data.errors, status=status.HTTP_400_BAD_REQUEST)
  
  elif request.method == 'DELETE':
    customer.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  

# Item CRUD functions (SRP)
@api_view(['GET', 'POST'])
def item_list(request):
  if request.method == 'GET':
    return get_item_list(request)
  elif request.method == 'POST':
    return create_item(request)

def get_item_list(request):
  items = Item.objects.all()
  serializer = ItemSerializer(items, many=True)
  return Response(serializer.data)

def create_item(request):
  serializer = ItemSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def item_details(request, id):
  item = get_item_object(id)

  if request.method == 'GET':
    return get_item_details(item)
  elif request.method == 'PUT':
    return update_item(item, request.data)
  elif request.method == 'DELETE':
    return delete_item(item)

def get_item_object(item_id):
  try:
    return Item.objects.get(pk=item_id)
  except Item.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

def get_item_details(item):
  serializer = ItemSerializer(item)
  return Response(serializer.data)

def update_item(item, data):
  item_data = ItemSerializer(item, data=data)
  if item_data.is_valid():
    item_data.save()
    return Response(item_data.data)
  return Response(item_data.errors, status=status.HTTP_400_BAD_REQUEST)

def delete_item(item):
  item.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)
