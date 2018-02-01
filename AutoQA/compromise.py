
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
# from ontobio.ontol_factory import OntologyFactory

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

class Compromise:
    def compromise(self):
        classCompromise = Compromise()
        qArry = classCompromise.qArry()
        aArry = classCompromise.aArry()
        random_index = randrange(0, len(qArry))
        questionStr = qArry[random_index]
        answerStr = aArry[random_index]

        #here we validate the created questions
        tool = language_check.LanguageTool('en-US')
        matchesQuestion = tool.check(questionStr)
        matchesAnswer = tool.check(answerStr)
        questionStr = language_check.correct(questionStr, matchesQuestion)
        answerStr = language_check.correct(answerStr, matchesAnswer)

        # url = "http://api.meaningcloud.com/stilus-1.2"
        #
        # payload = classCompromise.payload()
        # headers = {'content-type': 'application/x-www-form-urlencoded'}
        #
        # response = requests.request("POST", url, data=payload, headers=headers)
        #
        # print(response.text)
        #
        return "Question: " + questionStr + " </br> answer: " + answerStr

    def qArry(self):
        quesList = ["What is inheritance"]
        quesList.append("What is the four oop consepts")
        quesList.extend([
            "what is RAD stands for?",
            "How many phases RAD Model has?",
            "What is the major drawback of using RAD Model?",
            "What does SDLC stands for?",
            "Which model can be selected if user is involved in all the phases of SDLC?",
            "Explain what is meant by PRODUCT with reference to one of the eight principles as per the ACM/IEEE Code of Ethics ?",
            "What is a Software ?",
            "What are attributes of good software ?",
            "Mention two types of software products",
            "is Incremental Model an Evolutionary Process Model?",
            "What is the major advantage of using Incremental Model?",
            "How is WINWIN Spiral Model different from Spiral Model?",
            "Identify a disadvantage of Spiral Model.",
            "Does spiral Model has user involvement in all its phases.",
            "If you were to create client/server applications, which model would you go for?",
            "If you were a lead developer of a software company and you are asked to submit a project/product within a stipulated time-frame with no cost barriers, which model would you select?",
            "A company is developing an advance version of their current software available in the market, what model approach would they prefer ?",
            "What is a major advantage of using a 4GT Model for producing small scale products,applications or programs ?",
            "The RUP is normally described from three perspectives-dynamic, static & practice.What does static perspective do ?",
            "What does Agile Software Development is based on?",
            "How is plan driven development different from agile development ?",
            "How many phases are there in Scrum ?",
            "Which three framework activities are present in Adaptive Software Development(ASD) ?",
            "Which four framework activities are found in the Extreme Programming(XP) ?",
            "FAST stands for",
            "QFD stands for",
            "The user system requirements are the parts of which document ?",
            "Consider a system where, a heat sensor detects an intrusion and alerts the security company. What kind of a requirement the system is providing ?",
            "How many classification schemes have been developed for NFRs ?",
            "What are the four dimensions of Dependability ?",
            "What are the types of requirement in Quality Function Deployment(QFD) ?",
            "What are the kinds of actors used in OOSE ?",
            "How many Scenarios are there in elicitation activities ?",
            "What is the major drawback of CORE ?",
            "How is CORE different from IBIS ?",
            "How many steps are involved in Feature Oriented Domain Analysis (FODA) ?",
            "How many phases are there in Brainstorming ?",
            "How many feasibility studies is conducted in Requirement Analysis ?",
            "How many phases are there in Requirement Analysis ?",
            "The output of a program shall be given within 10secs of event X 10% of the time. What characteristic of SRS is being depicted here ?",
            "The data set will contain an end of file character. What characteristic of SRS is being depicted here ?",
        ])

        return quesList

    def aArry(self):
        ansList = ["this lets us build on privious work without reinventing the wheel"]
        ansList.append("encapsulation, inheritance, abstraction, polymorphism")
        ansList.extend([
            "Rapid Application Development",
            "5 phases",
            "Increases re-usability of components, Highly specialized & skilled developers/designers are required",
            "Software Development Life Cycle",
            "RAD Model",
            "Software engineers shall ensure that their products and related modifications meet the highest professional standards possible",
            "Software is set of programs, documentation & configuration of data",
            "Software maintainability & functionality",
            "Generic products and customized products",
            "No",
            "Easier to test and debug & It is used when there is a need to get a product to the market early",
            "It defines a set of negotiation activities at the beginning of each pass around the spiral",
            "Doesn’t work well for smaller projects",
            "No",
            "Concurrent Model",
            "RAD",
            "Both RAD & Iterative Enhancement",
            "Reduction in software development time",
            "It shows the process activities that are enacted",
            "Both Incremental and Iterative Development",
            "Iteration occurs within activities",
            "Three",
            "speculation, collaboration, learning",
            "planning, design, coding, testing",
            "Facilitated Application Specification Technique",
            "quality function deployment",
            "SRS",
            "Functional",
            "Five",
            "Availability, Reliability, Security, Safety",
            "Normal, Expected, Exciting",
            "Both Primary and Secondary",
            "Four",
            "Role of analyst is passive",
            "Consistency problems are addressed in CORE",
            "Three",
            "Three",
            "Three",
            "Five",
            "Verifiable",
            "Non-verifiable",
        ])
        return ansList

def OntologyQuestions():

        target = os.path.join(APP_ROOT, 'ExampleOntology/')
        if not os.path.isdir(target):
            os.mkdir(target)

        target = "".join([target, "nmrCV.owl"])
        #target = string.replace(target, '\'', '/')
        # print(target)

        #ont = OntologyFactory().create("file://"+target)
        ont = pronto.Ontology("http://nmrml.org/cv/v1.1.0/nmrCV.owl")
        # ont = pronto.Ontology("file:///"+target)
        print(ont.obo)
        print(ont.json)

        parentArry = []
        childrenArry = []

        for term in ont:
            if term.children:
                str = ""
                val = 1
                for itm in term.children.name:
                    if val ==1:
                        str = itm
                    else:
                        str = str + "," + itm
                    val = val+1

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



        #onto_path.append(target)
        #onto = get_ontology("file://E:/repository/intelligentRecruitment/AutoQA/ExampleOntology/dbpedia_2015-04.owl")
        #onto = get_ontology("file://"+target)
        # model = ontospy.Ontospy("http://www.lesfleursdunormal.fr/static/_downloads/pizza_onto.owl")
        # print(list(model.classes))
        #ont = pronto.Ontology('https://net.path.should/work/too.owl')
        #onto = get_ontology("http://tresetsolutions.000webhostapp.com/dbpedia_2015-04.owl") E:\repository\intelligentRecruitment\AutoQA\ExampleOntology/dbpedia_2015-04.owl
        #onto = get_ontology("http://www.lesfleursdunormal.fr/static/_downloads/pizza_onto.owl")
        #onto = get_ontology("http://webprotege.stanford.edu/#projects/87b9fe77-af8c-457a-bc5a-f1f598bf9082/edit/Classes?selection=Class(%3Chttp://webprotege.stanford.edu/R8StZAAxh566DvrwIPVwQfR%3E)")

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
            i = i+1

        print("**********************************************")
        print(childrenArry[20])
        print(parentArry[20])
        print("**********************************************")

        ontoQstArry = []
        ontoAnsArry = []
        i=0
        for itm in parentArry:
            if "," in childrenArry[i]:
                ontoQstArry.append("What are " + parentArry[i] + " ?")
                ontoAnsArry.append(childrenArry[i])
            else:
                ontoQstArry.append("What is " + parentArry[i] + " ?")
                ontoAnsArry.append(childrenArry[i])
            i = i+1

        ArryObj = {}
        ArryObj["ontoQstArry"] = ontoQstArry
        ArryObj["ontoAnsArry"] = ontoAnsArry

        return ArryObj
