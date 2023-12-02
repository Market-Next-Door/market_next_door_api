from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *

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
  
# Vendors 
@api_view(['GET', 'POST']) 
def vendor_list(request):
  
    if request.method == 'GET':
      vendors = Vendor.objects.all()
      serializer = VendorSerializer(vendors, many=True)
      return Response(serializer.data)
    
    elif request.method == 'POST':
      serializer = VendorSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      
@api_view(['GET', 'PUT', 'DELETE'])
def vendor_details(request, id):
  
    try:
      vendor = Vendor.objects.get(pk=id)
    except Vendor.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
      serializer = VendorSerializer(vendor)
      return Response(serializer.data)
    
    elif request.method == 'PUT':
      vendor_data = VendorSerializer(vendor, data=request.data)
      if vendor_data.is_valid():
        vendor_data.save()
        return Response(vendor_data.data)
      return Response(vendor_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
      vendor.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
  