from django.db import models
from store.models import Store
from tool.models import Tool
from django.db.models.signals import post_save, pre_save, pre_init , post_delete  

# Create your models here.


class Transfer(models.Model):
    Tool = models.ForeignKey(Tool,on_delete=models.CASCADE)
    StoreFrom = models.ForeignKey(Store,on_delete=models.CASCADE,related_name='storeFrom')
    StoreTo = models.ForeignKey(Store,on_delete=models.CASCADE,related_name='storeTo')
    Quantity = models.IntegerField(max_length=100)
    # date time

    created_at = models.DateTimeField(auto_now_add=True , null=True )
    created_by = models.ForeignKey('auth.User',on_delete=models.CASCADE,null = True)

    def _str_(self):
        return Tool.name
    
def TransferPostSave(sender,instance,*args,**kwargs):
    
    pass

def TransferPostDelete(sender,instance,**kwargs):
    storeFrom = Store.objects.all().filter(id = instance.StoreFrom.id).first()
    storeTo = Store.objects.all().filter(id = instance.StoreTo.id).first()  
    storeFrom.RealNumberTools -= instance.Quantity
    storeTo.RealNumberTools += instance.Quantity

post_save.connect(TransferPostSave,sender=Transfer)
post_delete.connect(TransferPostDelete,sender=Transfer)