# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Process

# Create your views here.

def index(request):
   #return HttpResponse("Hello user")
   
   return render(request, 'app/index.html')
