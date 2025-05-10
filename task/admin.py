from django.contrib import admin
from .models import MyTask
# Register your models here.

class MyTaskAdmin(admin.ModelAdmin):
    list_display=['id','name','desc']
    ordering=['id']
admin.site.register(MyTask,MyTaskAdmin)
