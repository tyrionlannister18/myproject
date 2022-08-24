from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=20)
    esal = models.IntegerField()
    ecity= models.CharField(max_length=20)

