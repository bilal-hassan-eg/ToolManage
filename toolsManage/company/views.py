from django.shortcuts import render
from django.http import HttpResponse
from store.models import Store
from tool.models import Tool
from company.models import Company
# Create your views here.

def CompanyStatistics(request,id,name):
    stores = Store.objects.all().filter(CompanyID=id)
    data = {'name' : name , 'stores' : stores , 'id' : id}
    return render(request,"sections/statisticsCompany.html",data)


def InsertCompany(request):
    f = open("companys.txt" , 'r' , encoding='utf-8')
    data = f.read()
    f.close()
    data1 = data.split('\n')
    for item in data1:
        data2 = item.split('|')
        if data2[0] != '' :
            print(data2[0] , data2[1])
            comp = Company.objects.create(name = data2[0].encode('utf-8') , numberStores = 0)
            comp.save()
    return HttpResponse("ok")

def resetCounter(request):
    companys = Company.objects.all()
    for comp in companys:
        comp.numberStores = 0
        comp.save()