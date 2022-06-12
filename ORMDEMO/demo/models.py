from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=30)
    esal = models.IntegerField()

class Student(models.Model):
    sid = models.IntegerField(primary_key=True)
    sname = models.CharField(max_length=30)
    age = models.IntegerField()