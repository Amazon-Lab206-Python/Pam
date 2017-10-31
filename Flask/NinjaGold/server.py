from flask import Flask, render_template, redirect, request, session
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key = "this is so secret"


@app.route('/')
def index():
    try:
        session['gold']
    except:
        session['gold'] = 0
        session['log'] = []
    return render_template('index.html')

@app.route('/process_money', methods=["POST"])
def money():
    if request.form['building'] == 'farm':
        farm_gold = random.randint(10,20)
        session['gold'] += farm_gold
        msg = "You earned {} gold from the farm! {}".format(farm_gold,datetime.now())
        session['log'].append(msg)
    elif request.form['building'] == 'cave':
        cave_gold = random.randint(5,10)
        session['gold'] += cave_gold
        msg = "You earned {} gold from the cave! {}".format(cave_gold, datetime.now())
        session['log'].append(msg)
    elif request.form['building'] == 'house':
        house_gold = random.randint(2,5)
        session['gold'] += house_gold
        msg = "You earned {} gold from the house! {}".format(house_gold, datetime.now())
        session['log'].append(msg)
    elif request.form['building'] == 'casino':
        winlose = random.randint(0,1)
        casino_gold = random.randint(0,50)
        if winlose == 0:
            session['gold'] -= casino_gold
            msg = "You lost {} gold at the casino. :( {}".format(casino_gold, datetime.now())
            session['log'].append(msg)
        else:
            session['gold'] += casino_gold
            msg = "You won {} gold at the casino! {}".format(casino_gold, datetime.now())
            session['log'].append(msg)
    return redirect('/')

@app.route('/reset', methods=["POST"])
def reset():
    session.clear()
    return redirect("/")

app.run(debug=True)