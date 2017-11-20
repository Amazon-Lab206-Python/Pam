# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User, Award, Location
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

def index(request):
    return render(request, "phone_tool/index.html")

def register(request):
    result = User.objects.validate_reg(request.POST)
    if result[0] == False:
        for error in result[1]:
            print error
            messages.error(request, error)
        return redirect("/")
    else:
        request.session['user_id'] = User.objects.get(email=request.POST['email']).id
        return redirect("/users/{}".format(request.session['user_id']))

def login(request):
    result = User.objects.validate_login(request.POST)
    if result[0] == False:
        for error in result[1]:
            print error
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['user_id'] = User.objects.get(email=request.POST['email']).id
        return redirect("/users/{}".format(request.session['user_id']))