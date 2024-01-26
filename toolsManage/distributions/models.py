from typing import Any
from django.db import models
from store.models import Store
from tool.models import Tool
from django.db.models.signals import post_save, pre_save, pre_init , post_delete  
from simple_history.models import HistoricalRecords
from simple_history.utils import update_change_reason
from log.models import Log
import datetime
# Create your models her.

class distribution(models.Model):
    tool = models.ForeignKey(Tool , on_delete=models.CASCADE)
    store = models.ForeignKey(Store , on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    changed_by = models.ForeignKey('auth.User',on_delete=models.CASCADE, null = True , default = 1)
    is_transfer = models.BooleanField(default=False)


    def __str__(self):
        return self.tool.name.name
    
# def distrubutePostSave(sender,instance,*args,**kwargs):
#     print(instance.reason_change)
#     update_change_reason(instance , instance.reason_change)

def distrubutePreSave(sender,instance,*args,**kwargs):
    dist = distribution.objects.filter(id = instance.id).first()
    op = True

    if dist:

        
        if dist.quantity > instance.quantity:
            op=False

        reason_change = ""
        if dist.store != instance.store:reason_change += "store " 
        if dist.quantity != instance.quantity:reason_change += "quantity " 
        if dist.tool != instance.tool:reason_change += "tool " 

        #update_change_reason(instance , reason_change)
    quant_sum = 0
    q = dist.quantity if dist else 0
    if op:
        quant_sum = (instance.quantity  -  (q))
        instance.store.numberTools += (instance.quantity  -  (q))
        instance.tool.name.numberTools +=  (instance.quantity  -  (q))
    else:
        print("HERE")
        print((dist.quantity  - q) , op)
        quant_sum = (dist.quantity  - instance.quantity)
        instance.store.numberTools -= (dist.quantity  - instance.quantity)
        instance.tool.name.numberTools -=  (dist.quantity  -  instance.quantity)
    instance.store.save()
    instance.tool.name.save()

    operation = "اضافة"
    if not op:
        operation = "سحب"
    if dist and not dist.is_transfer:
        log = Log.objects.create(store_from = instance.store,store_to = instance.store , tool = instance.tool , quantity = quant_sum, changed_by = instance.changed_by , date = datetime.datetime.now()
                                , operation = operation)
        log.save()
    
    if not dist and not instance.is_transfer:

        log = Log.objects.create(store_from = instance.store,store_to = instance.store , tool = instance.tool , quantity = instance.quantity , changed_by = instance.changed_by , date = datetime.datetime.now())
        log.save()



pre_save.connect(distrubutePreSave,sender=distribution)