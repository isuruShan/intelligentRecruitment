

import numpy as np
from random import randrange
import requests
import language_check
from owlready2 import *

from AutoQA.QCheckNLP import QCheckNLP
from .OntoCreate import *
import os
import ast
from .models import *
import string
import ontospy
import pronto
from pronto import Term, Relationship
# from ontobio.ontol_factory import OntologyFactory
import urllib.request
import shutil
from .ginger_python2 import *
import json
from collections import namedtuple
from django.utils.encoding import smart_str


class WeightAdd:

    def QuestionReform(self, ontoQstArry, ontoAnsArry):

        ontoQstArryConfidence = []
        ontoAnsArryConfidence = []

        for elemnt in ontoQstArry:
            data = json.dumps(get_ginger_result(elemnt))
            #FirstObj = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
            FirstObj = json.loads(data)
            for key in FirstObj:
                for innerKey in FirstObj[key]:
                    for innerInnerKey in innerKey:
                        #print(str(innerInnerKey) + ":" + str(innerKey[innerInnerKey]))
                        #if (isinstance(str(innerKey['Confidence']), str)):
                        ontoQstArryConfidence.append(str(innerKey['Confidence']))

        #InnerObj = FirstObj.LightGingerTheTextResult
        for elemnt in ontoAnsArry:
            data = json.dumps(get_ginger_result(elemnt))
            #FirstObj = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
            FirstObj = json.loads(data)
            for key in FirstObj:
                for innerKey in FirstObj[key]:
                    for innerInnerKey in innerKey:
                        print("check over")
                        #print(str(innerInnerKey) + ":" + str(innerKey[innerInnerKey]))
                        # if (isinstance(str(innerKey['Confidence']), str)):
                        #     ontoAnsArryConfidence.append(str(innerKey['Confidence']))

        ArryObj = {}
        ArryObj["ontoQstArry"] = ontoQstArry
        ArryObj["ontoAnsArry"] = ontoAnsArry
        ArryObj["ontoQstArryConfidence"] = ontoQstArryConfidence
        ArryObj["ontoAnsArryConfidence"] = ontoAnsArryConfidence
        return ArryObj