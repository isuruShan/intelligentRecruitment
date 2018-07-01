import requests
import json


def post(blob, fre):
    body = blob
    url1 = "http://localhost:8082/api/v1/speech_conf/alert"
    res = requests.post(url=url1, data= blob, headers={'Content-Type': 'application/octet-stream'})
    url2 = "http://localhost:8082/api/v1/speech_conf/alert2"
    res2 = requests.post(url=url2, data={'fre':fre}, headers={'Content-Type': 'application/json'})
    return res2.json()['result'], res.json()['success']

