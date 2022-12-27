from django.db import models
from django.db.models.signals import post_save, pre_save, pre_init
from django.dispatch import receiver
from django.db.models import F,Q
import socket
# Create your models here.

class info():
    LastIdToolName = 0
    hasattr(LastIdToolName,"id")

class Function(models.Model):
    name = models.CharField(max_length=100,null=True,unique=True,blank=False)
    def __str__(self) -> str:
        return self.name

class Tool(models.Model):
    name = models.ForeignKey('Function',on_delete=models.CASCADE,default=1)
    mac = models.CharField(max_length=100, null=True,unique=True,blank=True)
    ip = models.CharField(max_length=100, null=True,unique=True,blank=True)
    ssid = models.CharField(max_length=100, null=True,unique=False,blank=True)
    notes = models.CharField(max_length=100,null=True,unique=False,blank=True)
    StoreID = models.ForeignKey('Store',on_delete=models.CASCADE,default=1)

class Store(models.Model):
    name = models.CharField(max_length= 100 , null=True,unique=False,blank=False)
    location = models.CharField(max_length=100 , null=True,unique=False,blank=True)
    notes = models.TextField(null=True,unique=False,blank=True)
    CompanyID = models.ForeignKey('Company',on_delete=models.CASCADE)
    numberTools = models.IntegerField(editable=False,null=True)
    def __str__(self) -> str:
        return self.name
    
class Company(models.Model):
    name = models.CharField(max_length=100,null=True,unique=True,blank=False)
    def __str__(self) -> str:
        return self.name

class CompanyStatistics(models.Model):
    statisticsLink = models.CharField(max_length=100,null=True,unique=True,blank=True)
    CompanyID = models.ForeignKey("Company",null=True,on_delete=models.CASCADE)

def CompanyPreInit(sender,instance,*args,**kwargs):
    print("test")
    stats = CompanyStatistics.objects.all().filter(CompanyID=instance.id)
    if len(stats) == 0:
        data = Company.objects.all()
        for comp in data:
            if comp.id == instance.id:
                hostname = socket.gethostname()
                IPAddress = socket.gethostbyname(hostname)
                stat = CompanyStatistics()
                stat.CompanyID = instance
                stat.statisticsLink = "http://127.0.0.1:8000/CompanyStatistics/"
                #stat.statisticsLink = "https://{}/stats/name={}&id={}".format(IPAddress,comp.name,comp.id)
                print(stat.statisticsLink)
                stat.save()
            
post_save.connect(CompanyPreInit, sender=Company)