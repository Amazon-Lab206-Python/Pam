# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.utils.crypto import get_random_string

# Create your views here.

def index(request):
    context = {
        "date" : strftime("%m-%d-%Y",gmtime()),
        "time" : strftime("%H:%M", gmtime())
    }
    return render(request, "timedate/index.html", context)