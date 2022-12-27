from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group



# Register your models here.
class ToolsInlineTower(admin.TabularInline):
    model = Tool
    extra = 0

class CompanyStatisticsInline(admin.StackedInline):
    model = CompanyStatistics
    extra = 0
    can_delete = False
    

class StoreAdmin(admin.ModelAdmin):
    fields = ('name','location','notes','CompanyID')
    list_display = ('name','location','getType','getTools')
    list_filter = ('name' , 'location' , 'CompanyID')
    def getType(self, obj):
        data = obj.CompanyID
        return "{}".format(data)
    def getTools(self,obj):
        return len(Tool.objects.all().filter(StoreID=obj.id))
    inlines = [ToolsInlineTower]
    

class ToolAdmin(admin.ModelAdmin):
    fields = ('name', 'mac', 'ip', 'ssid', 'notes','StoreID')
    list_display = ('name', 'mac', 'ip', 'ssid', 'notes','StoreID')
    list_editable = ('ssid','StoreID')
    list_filter = ('name','StoreID')
    search_fields = ('ip', 'mac')

class CompanyAdmin(admin.ModelAdmin):
    fields = ("name" ,)
    list_display = ("name" , 'getStores')
    def getStores(self,obj):
        return len(Store.objects.all().filter(CompanyID=obj.id))
    list_filter = ('name',) 
    search_fields = ('name',)
    inlines = [CompanyStatisticsInline]
    
class FunctionAdmin(admin.ModelAdmin):
    fields = ("name" ,)
    list_display = ("name" ,'getTools')
    def getTools(self,obj):
        return len(Store.objects.all().filter(CompanyID=obj.id))
    list_filter = ('name',) 
    search_fields = ('name',)

admin.site.register(Function,FunctionAdmin)
admin.site.register(Store,StoreAdmin)
admin.site.register(Company,CompanyAdmin)
admin.site.register(Tool,ToolAdmin)

