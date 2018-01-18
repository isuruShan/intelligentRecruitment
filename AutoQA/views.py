from django.shortcuts import render
from django.http import HttpResponse
from .compromise import *

def index(request):
    str = "Hello this is view index method </br>"
    classCompromise = Compromise()
    str02 = ""
    for x in range(0, 9):
        str02 = classCompromise.compromise()
        str = str + "</br> </br>" + str02

    return HttpResponse (str)
