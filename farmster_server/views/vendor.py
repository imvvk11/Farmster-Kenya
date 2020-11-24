import json
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.views import APIView

# Models->
from farmster_server.models.vendor import Vendor

# Serializers->
from farmster_server.serializers.vendor import VendorSerializer

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum, Count, FloatField


class VendorCountAPIView(viewsets.ModelViewSet):
    serializer_class = VendorSerializer

    def get_queryset(self):
        queryset = Vendor.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        try:
            if request.data['phone'] == "":
                return Response({"Empty": "Please Enter Phone Number!"}, status=status.HTTP_204_NO_CONTENT)
            vendor = Vendor.objects.get(phone_number=request.data['phone_number'])
            vendor.count = vendor.count + 1
        except:
            vendor = Vendor()
            vendor.phone_number = request.data['phone_number']
            vendor.count = 1
        vendor.save()
        return Response({'message': [vendor.count]})
