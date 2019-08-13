from django.shortcuts import render
from django.http import HttpResponse
import os

def index(request):
    f = os.popen('../joy/sleuth --help')
    now = f.read()
    return HttpResponse(now)
