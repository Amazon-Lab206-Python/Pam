# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    try: 
        request.session['items']
    except: 
        request.session['items'] = 0
    try: 
        request.session['total']
    except: 
        request.session['total'] = 0
    return render(request, "amadon_buy/index.html")

def buy(request):
    if request.POST['product_id'] == '101':
        quantity = int(request.POST['quantity'])
        request.session['price'] = 19.99 * quantity
        request.session['items'] += quantity 
        request.session['total'] += request.session['price']
        print request.session['price']
        print request.session['items']
        print request.session['total']
    elif request.POST['product_id'] == '102':
        quantity = int(request.POST['quantity'])
        request.session['price'] = 29.99 * quantity
        request.session['items'] += quantity 
        request.session['total'] += request.session['price']
        print request.session['price']
        print request.session['items']
        print request.session['total']
    elif request.POST['product_id'] == '103':
        quantity = int(request.POST['quantity'])
        request.session['price'] = 4.99 * quantity
        request.session['items'] += quantity 
        request.session['total'] += request.session['price']
        print request.session['price']
        print request.session['items']
        print request.session['total']
    elif request.POST['product_id'] == '104':
        quantity = int(request.POST['quantity'])
        request.session['price'] = 49.99 * quantity
        request.session['items'] += quantity  
        request.session['total'] += request.session['price']
        print request.session['price']
        print request.session['items']
        print request.session['total']
    return redirect ('/checkout')

def checkout(request):
    return render(request, "amadon_buy/checkout.html")

def logout(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')
