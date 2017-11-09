# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from datetime import datetime

# Create your views here.
def index(request):
    try: 
        request.session['words']
    except: 
        request.session['words'] = []
    return render(request, "session_words/index.html")

def add(request):
    new_word = {}
    temp_list = request.session['words']
    is_big = request.POST.get('big', False)
    if request.POST['color'] == 'red' and not is_big:
        new_word['class'] = 'red'
        new_word['word'] = request.POST['word']
        new_word['datetime'] = datetime.now().strftime("%m-%d-%Y %I:%M %p")
        print new_word
        temp_list.append(new_word)
        request.session['words'] = temp_list
        print request.session['words']
    elif request.POST['color'] == 'red' and is_big:
        new_word['class'] = 'redbig'
        new_word['word'] = request.POST['word']
        new_word['datetime'] = datetime.now().strftime("%m-%d-%Y %I:%M %p")
        print new_word
        temp_list.append(new_word)
        request.session['words'] = temp_list
        print request.session['words']
    if request.POST['color'] == 'blue' and not is_big:
        new_word['class'] = 'blue'
        new_word['word'] = request.POST['word']
        new_word['datetime'] = datetime.now().strftime("%m-%d-%Y %I:%M %p")
        print new_word
        temp_list.append(new_word)
        request.session['words'] = temp_list
        print request.session['words']
    elif request.POST['color'] == 'blue' and is_big:
        new_word['class'] = 'bluebig'
        new_word['word'] = request.POST['word']
        new_word['datetime'] = datetime.now().strftime("%m-%d-%Y %I:%M %p")
        print new_word
        temp_list.append(new_word)
        request.session['words'] = temp_list
        print request.session['words']
    if request.POST['color'] == 'green' and not is_big:
        new_word['class'] = 'green'
        new_word['word'] = request.POST['word']
        new_word['datetime'] = datetime.now().strftime("%m-%d-%Y %I:%M %p")
        print new_word
        temp_list.append(new_word)
        request.session['words'] = temp_list
        print request.session['words']
    elif request.POST['color'] == 'green' and is_big:
        new_word['class'] = 'greenbig'
        new_word['word'] = request.POST['word']
        new_word['datetime'] = datetime.now().strftime("%m-%d-%Y %I:%M %p")
        print new_word
        temp_list.append(new_word) 
        request.session['words'] = temp_list 
        print request.session['words']  
    return redirect('/')

def clear(request):
    del request.session['words']
    return redirect('/')
