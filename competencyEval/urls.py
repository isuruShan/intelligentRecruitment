from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^index', interview_index),
    url(r'^transcribe', transcribe_view)
]