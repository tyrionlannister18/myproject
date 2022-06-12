from django.contrib import admin
from .models import Employee,Student
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eid','ename','esal']

class StudentAdmin(admin.ModelAdmin):
    list_display=['sid','sname','age']

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Student,StudentAdmin)