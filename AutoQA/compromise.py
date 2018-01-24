
import numpy as np
from random import randrange
import requests
import  language_check

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
        quesList = ["this is the start of questions set"]
        quesList.append("lets start")
        quesList.extend([
            "what is RAD stands for?",
            "How many phases RAD Model has?",
            "What is the major drawback of using RAD Model?",
            "What does SDLC stands for?",
            "Which model can be selected if user is involved in all the phases of SDLC?",
            "Explain what is meant by PRODUCT with reference to one of the eight principles as per the ACM/IEEE Code of Ethics ?",
            "is What a Software ?",
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
        ansList = ["this is the start of answer set"]
        ansList.append("lets start")
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

    def payload(self):
        key = ""
        lang = 'en-GB'
        txt = "how hello are you"
        url = ""
        doc = ""
