from django.shortcuts import render
from django.http import HttpResponse
from tool.models import Tool
from function.models import Function
from store.models import Store
# Create your views here.


def InsertTool(request):
    f = open("tools.txt" , 'r' , encoding='utf-8')
    data = f.read().split('\n')
    for item in data:
        data2 = item.split('|')
        #print(data2)
        func = Function.objects.filter(name = data2[0]).first()
        #store = Store.objects.filter(name = data2[6]).first()
        #print(func)
        print(Tool.objects.filter(name = func).first)
        if len(Tool.objects.filter(name = func , mac = data2[1] , ip = data2[2] , ssid = data2[3] , notes = data2[4])) == 0:
            print(data2)
            tool = Tool.objects.create(name = func , mac = data2[1] , ip = data2[2] , ssid = data2[3] , notes = data2[4])
            tool.save()
            #tool = Tool.objects.create()
        #line = tool.name.name + '|' + tool.mac + '|' + tool.ip + '|' + tool.ssid + '|'  + tool.notes  + '|' + str(tool.quantity) + '|' + tool.StoreID.name 
    return HttpResponse("OK")