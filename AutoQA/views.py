from django.shortcuts import render
from django.http import HttpResponse
from .compromise import *
from owlready2 import *
import urllib.request
import shutil
from .ginger_python2 import *
import json
from collections import namedtuple


def index(request):
    str = "Hello this is view index method </br>"
    classCompromise = Compromise()
    ArryObj = OntologyQuestions()
    ontoQstArry = ArryObj["ontoQstArry"]
    ontoAnsArry = ArryObj["ontoAnsArry"]

    str02 = ""
    for x in range(0, 3):
        str02 = classCompromise.compromise()
        str = str + "</br> </br>" + str02

    for x in range(3, 10):
        random_index = randrange(0, len(ontoQstArry))
        questionStr = ontoQstArry[random_index]
        answerStr = ontoAnsArry[random_index]
        str02 = "Question: " + questionStr + " </br> answer: " + answerStr
        str = str + "</br> </br>" + str02
        data = json.dumps(get_ginger_result(questionStr))
        FirstObj = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        print(FirstObj.LightGingerTheTextResult)
        print(data)


    #onto.save(target, "ont")

    # destination = "/".join([target, "ontol"])
    # with urllib.request.urlopen("http://www.lesfleursdunormal.fr/static/_downloads/pizza_onto.owl") as response, open("Onto.owl", 'wb') as destination:
    #     shutil.copyfileobj(response, destination)



    #InnerObj = FirstObj.LightGingerTheTextResult





    return HttpResponse(str)
