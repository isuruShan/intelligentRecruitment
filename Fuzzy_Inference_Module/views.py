from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def issa(request):
    return HttpResponse('issa')

def dula(request):
    return HttpResponse('dula')