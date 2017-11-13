# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import Course
from django.contrib.messages import error

# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, "courses/index.html", context)

def add(request):
    errors = Course.objects.validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message)
    else:
        Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
    return redirect('/')

def confirm(request, course_id):
    context = {
        'name': Course.objects.get(id=course_id).name,
        'desc': Course.objects.get(id=course_id).desc,
        'id': Course.objects.get(id=course_id).id
    }
    return render(request, "courses/confirm.html", context)

def destroy(request, course_id):
    Course.objects.get(id=course_id).delete()
    return redirect("/")