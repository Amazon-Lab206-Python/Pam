# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.

def index(request):
    try: 
        request.session['counter']
    except: 
        request.session['counter'] = 1
    context = {
        "randword" : get_random_string(length=14),
        "counter" : request.session['counter']
    }
    return render(request, "random_word/index.html", context)

def generate(request):
    request.session['counter'] += 1
    return redirect('/')

def reset(request):
    del request.session['counter']
    return redirect('/')