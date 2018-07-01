from __future__ import division

import nltk
import os
import wave
import numpy as np
import scipy.io.wavfile
import math
import argparse
import io
from django.shortcuts import render,render_to_response
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from pydub import AudioSegment
from django.views.decorators.csrf import csrf_exempt
from google.cloud import speech_v1p1beta1 as speech
from . similarity_check import para_similarity
from django.shortcuts import redirect
from .post_for_model import post
from .QA import SetOfQA
import json




# Create your views here.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#google cloude auth file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/isuru/PycharmProjects/gSpeechTest/MyFirstProject-28a3d7098e7b.json"

@csrf_exempt
def index(request):
    if request.method == 'GET':
        return render_to_response('clarify_category.html')
    elif request.method == 'POST':
        json_data = json.loads(request.body)
        request.session['uname'] = json_data['name']
        request.session['urole'] = json_data['role']
        request.session['qnum'] = 1
        result_1 = {'result': '1'}
        return JsonResponse(result_1)


def interview(request):
    print(request.session['qnum'])
    qnum = request.session['qnum']
    name = request.session['uname']
    list = SetOfQA.q_and_a()
    if qnum <= len(list):
        context = {
            'name' : name,
            'number': qnum,
            'question': list[qnum-1].q,
        }
        return  render_to_response('interview.html', context)
    else:
        return render_to_response('complete.html')


@csrf_exempt
def transcript(request):
    data = request.body
    file = wave.open("test_a.wav", "w")
    file.setnchannels(1)
    file.setsampwidth(4)
    file.setframerate(44100)
    file.writeframes(data)

    song = AudioSegment.from_wav("test_a.wav")
    song.export("test_af.flac", format="flac")

    # using deepgram brain to get the transcript
    client = speech.SpeechClient()

    with open("test_af.flac", 'rb') as audio_file:
        content = audio_file.read()
    audio = speech.types.RecognitionAudio(content=content)
    config = speech.types.RecognitionConfig(
        enable_automatic_punctuation=True,
        enable_word_time_offsets=True,
        encoding=speech.enums.RecognitionConfig.AudioEncoding.FLAC,
        language_code='en-US',
        model='default')

    response = client.recognize(config, audio)
    para_2 = ""
    start, end, word_counter = 0, 0, 0
    for i, result in enumerate(response.results):
        alternative = result.alternatives[0]
        print('-' * 20)
        # print('First alternative of result {}'.format(i))
        print('Transcript: {}'.format(alternative.transcript))
        para_2 += alternative.transcript

        for i in alternative.words:
            if word_counter == 0:
                start = i.start_time.seconds + i.start_time.nanos * 1e-9
            end = i.end_time.seconds + i.end_time.nanos * 1e-9
            word_counter += 1
    word_fre = word_counter*60/(end - start)
    print(word_counter*60/(end - start))
    res, res2 = post(data, word_fre)
    result_1 = {"result": para_2, "confidence": res}
    return JsonResponse(result_1)

@csrf_exempt
def decision(request):
    json_data = json.loads(request.body)
    qnum = request.session['qnum']
    user_answer = json_data['answer']
    user_confidence = json_data['confidence']
    list = SetOfQA.q_and_a()
    sys_answer = list[qnum-1].a
    similarity_score = para_similarity(
        user_answer, sys_answer)

    conf_value = 0
    if user_confidence == 0:
        conf_value = .3
    elif user_confidence == 1:
        conf_value = .1
    elif user_confidence == 2:
        conf_value = .6
    elif user_confidence == 3:
        conf_value = .3

    score = .3*conf_value + .7*similarity_score
    qnum += 1
    request.session['qnum'] = qnum
    return JsonResponse({'sucess':1})















###################################################################
        # file_name = "another.wav"
        # rate = 8000
        # data2 = np.asarray(request.GET.get('data'), dtype=np.int16)
        # response = HttpResponse(mimetype='audio/wav')
        # response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
        # response['Accept-Ranges'] = 'bytes'
        # response['X-Sendfile'] = smart_str(os.path.dirname(__file__))