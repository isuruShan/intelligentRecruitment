
import numpy as np
from random import randrange
import requests
import language_check
from owlready2 import *
import os
from .models import *
import string
import ontospy
import pronto
from pronto import Relationship
# from ontobio.ontol_factory import OntologyFactory

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

class QFormat:
    def OntologyQuestions(self):

        target = os.path.join(APP_ROOT, 'ExampleOntology\\')
        if not os.path.isdir(target):
            os.mkdir(target)

        target = "".join([target, "nmrCV.owl"])
        # target = string.replace(target, '\'', '/')
        # print(target)

        # ont = OntologyFactory().create("file://"+target)
        # ont = pronto.Ontology("http://nmrml.org/cv/v1.1.0/nmrCV.owl") #http://127.0.0.1:8000/AutoQA/ontoReturn
        # ont = pronto.Ontology("http://127.0.0.1:8000/AutoQA/ontoReturn")
        ont = pronto.Ontology(target)
        print(ont.obo)
        print("********************************* The Json Obj **************************************")
        print(ont.json)
        print("********************************* The Json Obj **************************************")
        for r in Relationship.topdown():
            print(r)
        print("********************************* The Json Obj Relationship Set **************************************")
        for relations in ont.json:
            print(relations)
        print("********************************* The Json Obj Relationship Set **************************************")
        parentArry = []
        childrenArry = []

        for term in ont:
            if term.children:
                str = ""
                val = 1
                for itm in term.children.name:
                    if val == 1:
                        str = itm
                    else:
                        str = str + "," + itm
                    val = val + 1

                childrenArry.append(str)
                if term.desc.strip() == "":
                    parentArry.append(term.name)
                else:
                    parentArry.append(term.desc)
                    # print(term)

        print("**********************************************")
        print(childrenArry[20])
        print(parentArry[20])
        print("**********************************************")

        # onto_path.append(target)
        # onto = get_ontology("file://E:/repository/intelligentRecruitment/AutoQA/ExampleOntology/dbpedia_2015-04.owl")
        # onto = get_ontology("file://"+target)
        # model = ontospy.Ontospy("http://www.lesfleursdunormal.fr/static/_downloads/pizza_onto.owl")
        # print(list(model.classes))
        # ont = pronto.Ontology('https://net.path.should/work/too.owl')
        # onto = get_ontology("http://tresetsolutions.000webhostapp.com/dbpedia_2015-04.owl") E:\repository\intelligentRecruitment\AutoQA\ExampleOntology/dbpedia_2015-04.owl
        # onto = get_ontology("http://www.lesfleursdunormal.fr/static/_downloads/pizza_onto.owl")
        # onto = get_ontology("http://webprotege.stanford.edu/#projects/87b9fe77-af8c-457a-bc5a-f1f598bf9082/edit/Classes?selection=Class(%3Chttp://webprotege.stanford.edu/R8StZAAxh566DvrwIPVwQfR%3E)")

        # onto.load()
        # print("****************************************")
        # print(onto.Award)
        # print(list(onto.classes()))
        # #print(list(onto.type))
        # print("****************************************")

        # c = CallObj()
        # c.x = 'foo'  # setter called
        # #print(c.x)
        # foo = c.x  # getter called
        # print(foo)
        # del c.x  # deleter called
        # #print(c.x)

        i = 0
        for elemnt in parentArry:
            if parentArry[i].strip() == "" or childrenArry[i].strip() == "":
                parentArry.remove(parentArry[i])
                childrenArry.remove(childrenArry[i])
            i = i + 1

        print("**********************************************")
        print(childrenArry[20])
        print(parentArry[20])
        print("**********************************************")

        ontoQstArry = []
        ontoAnsArry = []
        i = 0
        for itm in parentArry:
            if "," in childrenArry[i]:
                ontoQstArry.append("What are " + parentArry[i] + " ?")
                ontoAnsArry.append(childrenArry[i])
            else:
                ontoQstArry.append("What is " + parentArry[i] + " ?")
                ontoAnsArry.append(childrenArry[i])
            i = i + 1

        ArryObj = {}
        ArryObj["ontoQstArry"] = ontoQstArry
        ArryObj["ontoAnsArry"] = ontoAnsArry

        return ArryObj