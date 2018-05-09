from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^index', index),
    url(r'^codeSnippet', codeSnippet),
    url(r'^onCodePostButtonClick', onCodePostButtonClick),
]
