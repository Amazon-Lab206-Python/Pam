# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

# Create your views here.
def index(request):
    try:
        request.session['gold']
    except:
        request.session['gold'] = 0
        request.session['log'] = []
    return render(request, 'ninja_gold/index.html')

def process_money(request):
    new_log = {}
    temp_list = request.session['log']
    if request.POST['building'] == 'farm':
        farm_gold = random.randint(10,20)
        request.session['gold'] += farm_gold
        new_log['class'] = "win"
        new_log['msg'] = "You earned {} gold from the farm! ({})".format(farm_gold,datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        temp_list.append(new_log)
        request.session['log'] = temp_list
    elif request.POST['building'] == 'cave':
        cave_gold = random.randint(5,10)
        request.session['gold'] += cave_gold
        new_log['class'] = "win"
        new_log['msg'] = "You earned {} gold from the cave! ({})".format(cave_gold, datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        temp_list.append(new_log)
        request.session['log'] = temp_list
    elif request.POST['building'] == 'house':
        house_gold = random.randint(2,5)
        request.session['gold'] += house_gold
        new_log['class'] = "win"
        new_log['msg'] = "You earned {} gold from the house! ({})".format(house_gold, datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        temp_list.append(new_log)
        request.session['log'] = temp_list
    elif request.POST['building'] == 'casino':
        winlose = random.randint(0,1)
        casino_gold = random.randint(0,50)
        if winlose == 0:
            request.session['gold'] -= casino_gold
            new_log['msg'] = "You lost {} gold at the casino. :( ({})".format(casino_gold, datetime.now().strftime("%m-%d-%Y %I:%M %p"))
            new_log['class'] ="lose"
            temp_list.append(new_log)
            request.session['log'] = temp_list
        else:
            request.session['gold'] += casino_gold
            new_log['msg'] = "You won {} gold at the casino! ({})".format(casino_gold, datetime.now().strftime("%m-%d-%Y %I:%M %p"))
            temp_list.append(new_log)
            new_log['class'] = "win"
            request.session['log'] = temp_list
    return redirect('/')

def reset(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect("/")
