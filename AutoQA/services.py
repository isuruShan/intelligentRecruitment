
from django.http import HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from .compromise import *
from .QFormat import *
from django.shortcuts import render,render_to_response
from owlready2 import *


class services:
    def post_codeSnipet(self, script):

        language = "java"
        versionIndex = "0"
        clientId = "1c709bfe1a01e4f6bd8951326a5c5906"
        clientSecret = "8e076b3b04b9cb15fa42ac8ab46ef1b698d5ebb38452bb4a9743bbfdf624a665"
        headers = {
            'Content-Type': 'application/json',
        }
        url = 'https://api.jdoodle.com/execute'
        params = {"script": script, "language": language, "versionIndex": versionIndex, "clientId": clientId, "clientSecret": clientSecret }
        params = json.dumps(params)
        # params = json.loads(params)
        r = requests.post(url,  params, json, headers=headers )
        snippetResult = r.json()
        return snippetResult

    # send data
    # {
    # "script"	: "<?php print(\"hello world \"); ?>",
    # "language"	: "php",
    # "versionIndex"	: "0",
    # "clientId"	: "1c709bfe1a01e4f6bd8951326a5c5906",
    # "clientSecret"	: "8e076b3b04b9cb15fa42ac8ab46ef1b698d5ebb38452bb4a9743bbfdf624a665"
    # }
    #
    # recieved data
    # {
    #     "output": "hello world ",
    #     "statusCode": 200,
    #     "memory": "8028",
    #     "cpuTime": "0.00"
    # }