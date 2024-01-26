from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from simple_history import register
from .models import *
from tool.models import Tool
from django.contrib.auth.models import User

# Register your models here.


class ToolsInlineTower(admin.TabularInline):
    model = Tool
    extra = 0

class StoreAdmin(SimpleHistoryAdmin):
    fields = ('name','location','notes','CompanyID' , 'statisticsLink')
    list_display = ('name','location','CompanyID','numberTools')
    search_fields = ('name','location',)
    list_editable = ('CompanyID',)
    list_filter = ('name' , 'location' , 'CompanyID')
    object_history_form_template = 'history/historyStore.html'
    object_history_template = 'history/historyStore.html'
    #inlines = [ToolsInlineTower]

admin.site.register(Store,StoreAdmin)
