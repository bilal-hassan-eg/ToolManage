from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def CompanyStatistics(response):
    data = {'name':'sawa'}
    return render(response,"sections/statistics.html",data)