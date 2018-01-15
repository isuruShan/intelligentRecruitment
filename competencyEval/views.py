import nltk

from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from datetime import date
from django.contrib.auth.models import Permission
from django.utils.timezone import now
from django.db.models import Q


# Create your views here.


def transcribe_view(request):
    return render(request, 'cmp_transcribe.html')