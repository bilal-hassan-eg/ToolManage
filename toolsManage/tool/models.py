from django.db import models
from django.db.models.signals import post_save, pre_save, pre_init , post_delete  
import socket
from simple_history.utils import update_change_reason
from store.models import Store
from function.models import Function
from simple_history.models import HistoricalRecords
# Create your models here.


class Tool(models.Model):
    name = models.ForeignKey(Function,on_delete=models.CASCADE,default=1)
    mac = models.CharField(max_length=100, null=True,unique=False,blank=True)
    ip = models.CharField(max_length=100, null=True,unique=False,blank=True)
    ssid = models.CharField(max_length=100, null=True,unique=False,blank=True)
    notes = models.CharField(max_length=100,null=True,unique=False,blank=True)
    #quantity = models.IntegerField(max_length=100,null=True,default=1,blank=True)
    #StoreID = models.ForeignKey(Store,on_delete=models.CASCADE,default=1)
    changed_by = models.ForeignKey('auth.User',on_delete=models.CASCADE, null = True , default=1)

    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.name.name
    

def ToolPreSave(sender,instance,*args,**kwargs):
    tool = Tool.objects.all().filter(id = instance.id).first()  
    if not instance in Tool.objects.all():


        instance.reason_change = "New"

    else:
        reason_change = ""
        if tool.name != instance.name:reason_change += "name "
        if tool.ip != instance.ip:reason_change += "ip "
        if tool.mac != instance.mac:reason_change += "mac "
        if tool.ssid != instance.ssid:reason_change += "ssid "
        if tool.notes != instance.notes:reason_change += "notes "
        #if tool.quantity != instance.quantity:reason_change += "quantity "
        #if tool.StoreID != instance.StoreID:reason_change += "Store "

        instance.reason_change = reason_change

def ToolPostSave(sender,instance,*args,**kwargs):
    update_change_reason(instance,instance.reason_change)

# def ToolPostDelete(sender,instance,**kwargs):
#     store = Store.objects.all().filter(id = instance.StoreID.id).first()
#     store.RealNumberTools -= instance.quantity
#     store.numberTools -= instance.quantity
#     store.save()
    
post_save.connect(ToolPostSave,sender=Tool)
pre_save.connect(ToolPreSave,sender=Tool)
#post_delete.connect(ToolPostDelete,sender=Tool)