from django.http import HttpResponse
from django.shortcuts import render
import datetime

from django.template import loader, context

def home(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def aboutme(request):
    return render(request, 'aboutme.html')