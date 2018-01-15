from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from datetime import date
from django.contrib.auth.models import Permission
from django.utils.timezone import now
from django.db.models import Q


def login_view(request):

    return render_to_response('auth/login.html')


