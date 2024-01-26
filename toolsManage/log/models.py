from django.db import models
from store.models import Store
from tool.models import Tool

# Create your models here.

class Log(models.Model):
    store_from = models.ForeignKey(Store , on_delete=models.CASCADE , null=True,related_name="storeF")
    store_to = models.ForeignKey(Store , on_delete=models.CASCADE , null=True,related_name="storeT")
    tool = models.ForeignKey(Tool , on_delete=models.CASCADE , null=True)
    quantity = models.IntegerField(default=0 , null=False , blank=False)
    changed_by = models.ForeignKey('auth.User',on_delete=models.CASCADE, null = True , default=1)
    date = models.DateTimeField(null=False , blank=False)
    operation = models.CharField(choices=(
        ("اضافة", "اضافة"),
        ("سحب", "سحب"),
        ('نقل' , 'نقل')),default="اضافة",max_length=100)