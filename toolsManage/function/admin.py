from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import *
from simple_history.admin import SimpleHistoryAdmin
from simple_history import register
from tool.models import Tool
from django.contrib.auth.models import User

# Register your models here.


class FunctionAdmin(SimpleHistoryAdmin):
    fields = ("name" , 'statisticsLink')
    list_display = ("name" ,'getTools','numberTools')
    def getTools(self,obj):
        return len(Tool.objects.all().filter(name=obj.id))
    list_filter = ('name',) 
    search_fields = ('name',)
    object_history_form_template = 'history/historyFunction.html'
    object_history_template = 'history/historyFunction.html' 

admin.site.register(Function,FunctionAdmin)
