from django.shortcuts import render
from tool.models import Tool
from django.http import HttpResponse
from store.models import Store
from company.models import Company
from distributions.models import distribution
# Create your views here.

def StoreStatistics(request,id,name):
    dists = distribution.objects.filter(store__id = id)
    counter = 0 
    for dist in dists:
        counter += dist.quantity
    print(dists)
    data = {'name' : name , 'dists' : dists , 'numberTool' : counter}
    return render(request,"sections/statisticsStore.html",data)

def InsertStore(request):
    f = open("stores.txt" , 'r' , encoding='utf-8')
    data = f.read()
    data1 = data.split('\n')
    for item in data1:
        data2 = item.split('|')
        #line = store.name + '|' + store.location + '|' + store.notes + '|' + str(store.numberTools)
        if(data2[0] != ''):
            comp = Company.objects.filter(name = data2[4]).first()
            store = Store(name = data2[0] , location = data2[1] , notes = data2[2] , numberTools = 0 , CompanyID = comp)
            store.save()
    return HttpResponse("OK")

def resetCounter(rquest):
    stores = Store.objects.all()
    for store in stores:
        store.numberTools = 0
        store.save()