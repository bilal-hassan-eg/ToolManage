from django.db import models
import socket
from simple_history.utils import update_change_reason
from simple_history.models import HistoricalRecords
from django.db.models.signals import post_save, pre_save, pre_init , post_delete 

# Create your models here.

class Function(models.Model):
    name = models.CharField(max_length=100,null=True,unique=True,blank=False)
    statisticsLink = models.URLField(max_length=100,null=True,unique=True,blank=True,default=None,db_index=True)    
    numberTools = models.IntegerField(max_length=100,default=0)
    changed_by = models.ForeignKey('auth.User',on_delete=models.CASCADE,null = True)

    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.name
    
def FunctionPostSave(sender,instance,*args,**kwargs):
    if not instance.statisticsLink:
        hostname = socket.gethostname()
        IPAddress = socket.gethostbyname(hostname)
        FunctionName = instance.name.replace(' ', '_')
        function = Function.objects.all().filter(id = instance.id).first()
        function.statisticsLink = "http://{}:8000/FunctionStatistics/{}-{}".format(IPAddress,instance.id,FunctionName)
        function.save()
    update_change_reason(instance,instance.reason_change)    

def FunctionPreSave(sender,instance,*args,**kwargs):
    function = Function.objects.all().filter(id = instance.id).first()
    instance.reason_change = "New"
    if function:
        reason_change = ""
        if function.name != instance.name:reason_change += "name " 
        instance.reason_change = reason_change

post_save.connect(FunctionPostSave, sender=Function)
pre_save.connect(FunctionPreSave , sender=Function)