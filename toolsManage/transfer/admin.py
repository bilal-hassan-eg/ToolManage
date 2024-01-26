from django.contrib import admin
from .models import Transfer
from simple_history.admin import SimpleHistoryAdmin
# Register your models here.


class TransferAdmin(admin.ModelAdmin):
    #fields = ('name', 'mac', 'ip', 'ssid', 'notes','StoreID','quantity')
    list_display = ('Tool', 'StoreFrom', 'StoreTo', 'Quantity', 'created_at','created_by','cancell')
    #list_editable = ('StoreFrom','StoreTo','Quantity')
    list_filter = ('Tool','StoreFrom','StoreTo')

# admin.site.register(Transfer,TransferAdmin)