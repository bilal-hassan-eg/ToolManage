from django.db import models
from django.db.models.signals import post_save, pre_save, pre_init , post_delete 
import socket
from company.models import Company
from simple_history.models import HistoricalRecords
from simple_history.utils import update_change_reason
# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length= 100 , null=True,unique=False,blank=False)
    location = models.CharField(max_length=100 , null=True,unique=False)
    notes = models.TextField(null=True,unique=False,blank=True)
    CompanyID = models.ForeignKey(Company,on_delete=models.CASCADE)
    statisticsLink = models.URLField(max_length=100,null=True,unique=True,blank=True,default=None,db_index=True)
    numberTools = models.IntegerField(max_length=100,default=0)
    #RealNumberTools = models.IntegerField(max_length=100,default=0)
    changed_by = models.ForeignKey('auth.User',on_delete=models.CASCADE , null = True)

    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    def __str__(self):
        return self.name
    

def StorePostSave(sender,instance,*args,**kwargs):
    print(instance.location)
    if not instance.statisticsLink:
        hostname = socket.gethostname()
        IPAddress = socket.gethostbyname(hostname)
        storeName = instance.name.replace(' ', '_')
        store = Store.objects.all().filter(id = instance.id).first()
        store.statisticsLink = "http://{}:8000/StoreStatistics/{}-{}".format(IPAddress,instance.id,storeName)
        store.save()
    update_change_reason(instance,instance.reason_change)    

def StorePreSave(sender,instance,*args,**kwargs):
    store = Store.objects.all().filter(id=instance.id).first()    
    if not instance in Store.objects.all():
        company = Company.objects.all().filter(id=instance.CompanyID.id).first()
        company.numberStores += 1
        company.save()
        instance.reason_change = "New"
    else:
        if instance.CompanyID.id == store.CompanyID.id:
            pass
        else:
            oldComp = Company.objects.all().filter(id=store.CompanyID.id).first()
            oldComp.numberStores -= 1
            oldComp.save()
            company = Company.objects.all().filter(id=instance.CompanyID.id).first()
            company.numberStores += 1
            company.save()
    
        reason_change = ""

        if store.name != instance.name:reason_change += "name "
        if store.location != instance.location:reason_change += "location "
        if store.notes != instance.notes:reason_change += "notes "
        if store.CompanyID != instance.CompanyID:reason_change += "CompanyID "

        instance.reason_change = reason_change

def StorePostDelete(sender,instance,**kwargs):
    company = Company.objects.all().filter(id = instance.CompanyID.id).first()
    company.numberStores -= 1
    company.save()

post_save.connect(StorePostSave, sender=Store)
pre_save.connect(StorePreSave,sender=Store)
post_delete.connect(StorePostDelete,sender=Store)