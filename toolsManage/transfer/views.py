from django.shortcuts import render
from django.http import HttpResponse
from tool.models import Tool
from store.models import Store
from distributions.models import distribution
from django.http import JsonResponse
from function.models import Function
import json
from log.models import Log
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import datetime
# Create your views here.

def Transfer(request):
    tool = Tool.objects.all()
    store = Store.objects.all()
    dist = distribution.objects.all()
    funcs = Function.objects.all()
    print(dist)
    data = {'tools' : tool , 'stores' : list(store) , 'dists' : list(dist) , 'funcs' : funcs}
    return render(request,"transfer/index.html",data)


@csrf_exempt
def doTransfer(request):
    print(request.body.decode('utf-8'))
    data = json.loads(request.body.decode('utf-8'))

    store_from = data['store_from']
    store_to = data['store_to']
    tool = data["tool"]
    quantity = data["quantity"]
    print(store_to , store_from , tool , quantity)
    trans(store_from , store_to , tool , quantity)
    return HttpResponse("Done")


def trans(store_from , store_to , tool , quantity):
    store_toOBJ = distribution.objects.filter(store__name = store_to).first()
    store_fromOBJ = distribution.objects.filter(store__name = store_from).first()
    tool = Tool.objects.filter(name__name = tool).first()
    store_fromOBJ.quantity -= int(quantity)
    if store_toOBJ:
        store_toOBJ.quantity += int(quantity)
        store_toOBJ.save()
        log = Log.objects.create(store_from = store_fromOBJ.store,store_to = store_toOBJ.store , tool = tool , quantity = quantity , date = datetime.datetime.now()
                             , operation = "نقل")
        log.save()
    else:
        store = Store.objects.filter(name = store_to).first()
        dist = distribution.objects.create(store = store , tool = tool , quantity = int(quantity) , is_transfer = True)
        log = Log.objects.create(store_from = store_fromOBJ.store,store_to = store , tool = tool , quantity = quantity , date = datetime.datetime.now()
                             , operation = "نقل")
        log.save()
    store_fromOBJ.save()


    pass
