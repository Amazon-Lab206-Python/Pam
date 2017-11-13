# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.messages import error
import bcrypt

# Create your views here.
def index(request):
    return render(request, "login_reg/index.html")

def register(request):
    result = User.objects.validate_reg(request.POST)
    if len(result) > 0:
        for error in result:
            messages.error(request, error)
        return redirect("/")
    else:
        request.session['user_id'] = User.objects.get(email=request.POST['email']).id
        messages.success(request, "Thank you for registering")
        return redirect("/success")

def login(request):
    result = User.objects.validate_login(request.POST)
    if len(result) > 0:
        for error in result:
            messages.error(request, error)
        return redirect("/")
    else:
        request.session['user_id'] = User.objects.get(email=request.POST['email']).id
        messages.success(request, "Thank you for logging in")
        return redirect("/success")

def success(request):
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    print context
    return render(request, "login_reg/success.html", context)

def logout(request):
    del request.session['user_id']
    return redirect('/')