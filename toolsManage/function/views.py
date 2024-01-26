from django.shortcuts import render
from tool.models import Tool
from django.http import HttpResponse
from function.models import Function
# Create your views here.


def FunctionStatistics(request,idFunc,nameFunc):
    tools = Tool.objects.all().filter(name = idFunc)
    counterQuantity = 0
    print(len(tools), idFunc)
    data = {'name' : nameFunc , 'tools' : tools , 'numberTool' : counterQuantity} 
    return render(request,"sections/StatisticsFunction.html",data)
 
def InsertFunction(requet):
    f = open("functions.txt" , 'r' , encoding='utf-8')
    data = f.read().split('\n')
    for item in data:
        data2 = item.split('|')
        print(data2)
        function = Function.objects.create(name = data2[0] , numberTools = data2[1])
        function.save()
    return HttpResponse('OK')

def resetCounter():
    funcs = Function.objects.all()
    for func in func:
        func.numberTools = 0