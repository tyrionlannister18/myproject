from django.shortcuts import render
from .models import Employee,Student
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def about(r):
    # data2 = Student.objects.all()
    data2 = Student.objects.get(sname__exact='Amit')
    return render(r,'demo/about.html',{"data2":data2})

def contact(r):
    return render(r,'demo/contact.html')

def home(r):
    data = Employee.objects.all()
