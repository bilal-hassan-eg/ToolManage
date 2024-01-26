from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import distribution
# Register your models here.

class distAdmin(admin.ModelAdmin):
    list_display = ("tool" , 'store', 'quantity' , 'changed_by')
    list_filter = ('tool' , 'store' ,)

admin.site.register(distribution,distAdmin)
