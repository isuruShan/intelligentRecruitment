
from django.http import HttpResponse
from .compromise import *
from .QFormat import *
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

def ontoReturn(request):
    target = os.path.join(APP_ROOT, 'ExampleOntology')
    if not os.path.isdir(target):
        os.mkdir(target)

    target = os.path.join(target, 'nmrCV.owl')
    #target = "".join([target, " [ nmrCV.owl"])
    #target.replace('[', '\'')
    # print(target)

    # ont = OntologyFactory().create("file://"+target)
    #ont = pronto.Ontology("http://nmrml.org/cv/v1.1.0/nmrCV.owl")
    #ont = pronto.Ontology("file:///"+target)

    #response = HttpResponse(mimetype='application/force-download')  # mimetype is replaced by content_type for django 1.7
    #response['Content-Disposition'] = 'attachment; filename=%s' % smart_str("nmrCV.owl")
    #response['X-Sendfile'] = smart_str(target)
    #response = HttpResponse(content_type='application/force-download')

    #return HttpResponse(target)
    # It's usually a good idea to set the 'Content-Length' header too.
    # You can also set any other required headers: Cache-Control, etc.

    # code    to     check or protect    the    file    from unauthorized access
    response = HttpResponse()
    response['X-File'] = target
    #return response['X-File']

    return response