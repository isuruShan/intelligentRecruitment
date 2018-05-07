
from django.http import HttpResponse
from .compromise import *
from .QFormat import *
from django.shortcuts import render,render_to_response
from owlready2 import *


def index(request):
    str = "Hello this is view index method </br>"
    classCompromise = Compromise()
    QFormatClass = QFormat()


    ArryObj = QFormatClass.OntologyQuestions()
    ontoQstArry = ArryObj["ontoQstArry"]
    ontoAnsArry = ArryObj["ontoAnsArry"]

    str02 = ""
    # for x in range(0, 3):
    #     str02 = classCompromise.compromise()
    #     str = str + "</br> </br>" + str02

    for x in range(0, 10):
        random_index = randrange(0, len(ontoQstArry))
        questionStr = ontoQstArry[random_index]
        answerStr = ontoAnsArry[random_index]
        str02 = "Question: " + questionStr + " </br> answer: " + answerStr
        str = str + "</br> </br>" + str02

    return HttpResponse(str)

def codeSnippet(request):
    return render_to_response('AutoQATemplates/code_compare.html')