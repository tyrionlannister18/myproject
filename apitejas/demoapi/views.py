from django.shortcuts import render
from .models import Device
from .serializers import DeviceSer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class Deviceview(APIView):
    def get(self,r):
        ddata = Device.objects.all()
        serdata = DeviceSer(ddata,many=True)
        return Response(serdata.data)

    def post(self,r):
        serobj = DeviceSer(data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_201_CREATED)
        return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,r,x):
        ddata = Device.objects.get(did=x)
        serdata = DeviceSer(ddata,data=r.data)
        if serdata.is_valid():
            serdata.save()
            return Response(serdata.data,status=status.HTTP_201_CREATED)
        return Response(serdata.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,r,x):
        ddata = Device.objects.get(did=x)
        ddata.delete()
        return Response(status=status.HTTP_200_OK)