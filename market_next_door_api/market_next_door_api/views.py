from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomerSerializer
from .models import *

@api_view(['GET', 'POST']) 
def customer_list(request):

  if request.method == 'GET':
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)
  
  if request.method == 'POST':
    pass