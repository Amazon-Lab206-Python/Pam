# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib.messages import error

# Create your views here.

def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, "users/index.html", context)

def new(request):
    return render(request, "users/new.html")

def edit(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, "users/edit.html", context)

def show(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, "users/info.html", context)

def create(request):
    errors = User.objects.validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
                error(request, message)
        return redirect("/users/new")
    else:
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
    return redirect("/users")

def destroy(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect("/users")

def update(request, user_id):
    errors = User.objects.validate(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect("/users/{}/edit".format(user_id))
    else:
        user_update = User.objects.get(id = user_id)
        user_update.first_name = request.POST['first_name']
        user_update.last_name = request.POST['last_name']
        user_update.email = request.POST['email']
        user_update.save()
    return redirect("/users/{}".format(user_id))
