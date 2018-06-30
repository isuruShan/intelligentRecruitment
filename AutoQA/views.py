
from django.http import HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from .compromise import *
from .services import *
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

    for x in range(0, 10):
        random_index = randrange(0, len(ontoQstArry))
        questionStr = ontoQstArry[random_index]
        answerStr = ontoAnsArry[random_index]
        str02 = "Question: " + questionStr + " </br> answer: " + answerStr
        str = str + "</br> </br>" + str02

    return HttpResponse(str)

def codeSnippet(request):
    return render_to_response('AutoQATemplates/code_compare.html')

@csrf_exempt
def onCodePostButtonClick(request):
    if request.method == 'GET':
        print("method is get")
    elif request.method == 'POST':
        print("method is post")

    nameStr = request.POST['nameStr']
    click = request.POST['click']
    print(nameStr)
    print(click)

    message = 'WelDone'
    ClassServices = services()
    snippetResult = ClassServices.post_codeSnipet(str(nameStr))
    #snippetResult = json.loads(snippetResult)


    output = snippetResult['output']
    statusCode = snippetResult['statusCode']
    memory = snippetResult['memory']
    cpuTime = snippetResult['cpuTime']

    print(output)
    print(statusCode)
    print(memory)
    print(cpuTime)

    return HttpResponse(statusCode)