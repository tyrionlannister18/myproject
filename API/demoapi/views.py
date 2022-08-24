from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class Employeeview(APIView):
    def get(self,r):
        edata = Employee.objects.all()
        serdata = EmployeeSer(edata,many=True)
        return Response(serdata.data)

    def post(self,r):
        serobj = EmployeeSer(data = r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_201_CREATED)
        return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)


    def put(self,r,x):
        edata = Employee.objects.get(eid=x)
        serdata=EmployeeSer(edata,data=r.data)
        if serdata.is_valid():
            serdata.save()
            return Response(serdata.data,status=status.HTTP_201_CREATED)
        return Response(serdata.errors,stat=status.HTTP_400_BAD_REQUEST)

    def delete(self,r,x):
        edata = Employee.objects.get(eid=x)
        edata.delete()
        return Response(status=status.HTTP_200_OK)

