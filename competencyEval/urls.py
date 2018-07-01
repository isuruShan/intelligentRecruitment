from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^interview', interview, name='interview'),
    url(r'^home', index),
    url(r'^transcript', transcript),
    url(r'^decision', decision),
]