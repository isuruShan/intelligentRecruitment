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




# Create your views here.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#google cloude auth file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/isuru/PycharmProjects/gSpeechTest/MyFirstProject-28a3d7098e7b.json"


def index(request):
    return redirect('interview', backend=2, question='what is java?')


def interview_index(request):


    return render_to_response('cmp_transcribe.html')

def interview(request, backend, question):
    context = {
        'number': backend,
        'question': question
    }
    return  render_to_response('interview.html', context)

@csrf_exempt
def transcribe_view(request):
    data = request.body
    file = wave.open("test_audio4.wav","w")
    file.setnchannels(1)
    file.setsampwidth(2)
    file.setframerate(8000)
    file.writeframes(data)



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
    para_similarity("Java is a Murray riding programming language, which is very good language to build a pond.", para_2)
    result_1 = {"result": para_2}

    return JsonResponse(result_1)


@csrf_exempt
def transcript(request):
    data = request.body
    print(data)
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
    print(start)
    print(end)
    print(word_counter)
    print(word_counter*60/(end - start))
    similarity_score = para_similarity("Java is a Murray riding programming language, which is very good language to build a pond.",para_2)
    result_1 = {"result": para_2,  "score": round(similarity_score,2)}
    print(similarity_score)
    return JsonResponse(result_1)










###################################################################
        # file_name = "another.wav"
        # rate = 8000
        # data2 = np.asarray(request.GET.get('data'), dtype=np.int16)
        # response = HttpResponse(mimetype='audio/wav')
        # response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
        # response['Accept-Ranges'] = 'bytes'
        # response['X-Sendfile'] = smart_str(os.path.dirname(__file__))