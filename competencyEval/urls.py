from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^index/(?P<backend>\w+?)/(?P<question>.+?)/$', interview_index),
    url(r'^transcribe', transcribe_view),
    url(r'^interview/(?P<backend>\w+?)/(?P<question>.+?)/$', interview, name='interview'),
    url(r'^home', index),
    url(r'^transcript', transcript),
]