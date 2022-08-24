from django.db import models

# Create your models here.
class Device(models.Model):
    did = models.IntegerField(primary_key=True)
    manufacture = models.CharField(max_length=10)
    freq = models.IntegerField()
    model = models.CharField(max_length=20)


