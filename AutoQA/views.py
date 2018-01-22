from django.shortcuts import render
from django.http import HttpResponse
from .compromise import *

from owlready2 import *
import urllib.request
import shutil


APP_ROOT = os.path.dirname(os.path.abspath(__file__))

def index(request):
    str = "Hello this is view index method </br>"
    classCompromise = Compromise()
    str02 = ""
    for x in range(0, 9):
        str02 = classCompromise.compromise()
        str = str + "</br> </br>" + str02

    target = os.path.join(APP_ROOT, 'ExampleOntology/')
    if not os.path.isdir(target):
        os.mkdir(target)

    onto_path.append(target)
    onto = get_ontology("http://www.lesfleursdunormal.fr/static/_downloads/pizza_onto.owl")
    onto.load()
    #onto.save(target, "ont")

    destination = "/".join([target, "ontol"])
    with urllib.request.urlopen("http://www.lesfleursdunormal.fr/static/_downloads/pizza_onto.owl") as response, open("Onto", 'wb') as destination:
        shutil.copyfileobj(response, destination)

    return HttpResponse(str)
