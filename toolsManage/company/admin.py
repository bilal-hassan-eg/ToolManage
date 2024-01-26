from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from simple_history import register
from .models import Company
from django.contrib.auth.models import User

# Register your models here.

class CompanyAdmin(SimpleHistoryAdmin):
    fields = ("name", 'statisticsLink')
    list_display = ("name" , 'numberStores' )
    list_filter = ('name',) 
    search_fields = ('name',)
    object_history_form_template = 'history/historyCompany.html'
    object_history_template = 'history/historyCompany.html'

admin.site.register(Company,CompanyAdmin)