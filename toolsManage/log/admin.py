from django.contrib import admin
from .models import Log
# Register your models here.

class LogAdmin(admin.ModelAdmin):
    list_display= ('store_from' , 'store_to' , 'tool' , 'quantity' , 'changed_by' , 'date' , 'operation')
    list_filter= ('store_from' , 'store_to' , 'tool' , 'quantity' , 'changed_by' , 'date' , 'operation')

admin.site.register(Log,LogAdmin)