from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from simple_history import register
from .models import *
from django.contrib.auth.models import User
from distributions.models import distribution
# Register your models here.

class DistrubutionInline(admin.TabularInline):
    model = distribution
    extra = 0

class ToolAdmin(SimpleHistoryAdmin):
    object_history_form_template = 'history/historyTool.html'
    object_history_template = 'history/historyTool.html'
    fields = ('name', 'mac', 'ip', 'ssid', 'notes')
    list_display = ('name', 'notes' , 'ssid', 'mac' , 'getToolQuantity')
    #list_editable = ('quantity' ,)
    list_filter = ('name' , )
    search_fields = ('ip', 'mac','ssid','notes', )
    inlines = (DistrubutionInline , )

    def getToolQuantity(self,obj):
        dists = distribution.objects.filter(tool__name__name = obj)
        counter = 0
        for dist in dists:
            counter += dist.quantity
        return counter

admin.site.register(Tool,ToolAdmin)
