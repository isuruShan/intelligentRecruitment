from __future__ import division

import nltk
import os
import numpy as np
import scipy.io.wavfile
import math
import argparse
import io
from django.shortcuts import render,render_to_response
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from pydub import AudioSegment
from django.views.decorators.csrf import csrf_exempt
#from google.cloud import speech_v1p1beta1 as speech #this only for below versions of google-cloud 0.28.1
from google.cloud import speech #this is for after versions of google-cloud 0.32.0
from . similarity_check import para_similarity



# Create your views here.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#google cloude auth file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/isuru/PycharmProjects/gSpeechTest/MyFirstProject-28a3d7098e7b.json"


def interview_index(request):


    return render_to_response('cmp_transcribe.html')


@csrf_exempt
def transcribe_view(request):
    data = request.body
    file_name = os.path.join(
        os.path.dirname(__file__),
        'test.wav')
    song = AudioSegment.from_wav(file_name)
    song = song.set_channels(1)
    song.export("testme.flac", format="flac")
    result_1 = {"result": "hello"}

    # obviously handle correct naming of the file and place it somewhere like media/uploads/
    uploadedFile = open("recording.wav", "wb")
    # the actual file is in request.body
    uploadedFile.write(data)

    uploadedFile.close()

    #using deepgram brain to get the transcript
    client = speech.SpeechClient()

    with open("ExternalFiles/Recording_3.wav", 'rb') as audio_file:
        content = audio_file.read()
    audio = speech.types.RecognitionAudio(content=content)
    config = speech.types.RecognitionConfig(
        enable_automatic_punctuation=True,
        enable_word_time_offsets=True,
        encoding=speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code='en-US',
        model='default')

    response = client.recognize(config, audio)
    para_2 = ""

    for i, result in enumerate(response.results):
        alternative = result.alternatives[0]
        print('-' * 20)
        # print('First alternative of result {}'.format(i))
        print('Transcript: {}'.format(alternative.transcript))
        para_2 = alternative.transcript
    para_similarity("java is good a murray riding programming language for a pond. this is good for a pond", para_2)


    return JsonResponse(result_1)






###################################################################
        # file_name = "another.wav"
        # rate = 8000
        # data2 = np.asarray(request.GET.get('data'), dtype=np.int16)
        # response = HttpResponse(mimetype='audio/wav')
        # response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
        # response['Accept-Ranges'] = 'bytes'
        # response['X-Sendfile'] = smart_str(os.path.dirname(__file__))