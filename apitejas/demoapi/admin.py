from django.contrib import admin
from .models import Device
# Register your models here.
class DeviceAdmin(admin.ModelAdmin):
    list_display = ["did","manufacture","freq","model"]
admin.site.register(Device,DeviceAdmin)