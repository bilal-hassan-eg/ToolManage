from django.db import models
import socket
from simple_history.models import HistoricalRecords
from simple_history.utils import update_change_reason
from django.db.models.signals import post_save, pre_save, pre_init , post_delete 
# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100,null=True,unique=True)
    statisticsLink = models.URLField(max_length=100,null=True,unique=True,blank=True,default=None,db_index=True)
    numberStores = models.IntegerField(max_length=100,default=0)
    changed_by = models.ForeignKey('auth.User',on_delete=models.CASCADE ,null = True)

    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.name
    

def CompanyPostSave(sender,instance,*args,**kwargs):
    
    if not instance.statisticsLink:
        hostname = socket.gethostname()
        IPAddress = socket.gethostbyname(hostname)
        compName = instance.name.decode('utf-8').replace(' ', '_')
        #compName = instance.name.replace(' ', '_')
        comp = Company.objects.all().filter(id = instance.id).first()
        comp.name = instance.name.decode('utf-8')
        #comp.name = instance.name
        comp.statisticsLink = "http://{}:8000/CompanyStatistics/{}-{}".format(IPAddress,instance.id,compName)
        comp.save()
    if Company.objects.all().filter(id = instance.id).first():
        update_change_reason(instance,instance.reason_change)

def CompanyPreSave(sender,instance,*args,**kwargs):
    company = Company.objects.all().filter(id = instance.id).first()
    instance.name = instance.name
    print('TEST1 : ' , instance.name)
    if company :
        pass
        reason_change = ''
        if company.name != instance.name:reason_change += "name "
        instance.reason_change = reason_change
    else:
        instance.reason_change = "New"
pre_save.connect(CompanyPreSave,sender=Company)
post_save.connect(CompanyPostSave, sender=Company)
