from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "this is so secret"

import random

@app.route('/')
def index():
    try:
        session['winner']
    except:
        session['winner'] = random.randint(0,100)
    print session['winner']
    return render_template('index.html')

@app.route('/guess', methods=["POST"])
def guess():
    guess = request.form['guess']
    guess = int(guess)
    print guess
    print session['winner']
    if session['winner'] == guess:
        answer = "You Got It! Please Play Again..."
        session.pop('winner')
        return render_template('index.html', answer=answer)
    elif guess > session['winner']:
        answer = "Too High...Try again..."
        return render_template('index.html', answer=answer)
    elif guess < session['winner']:
        answer = "Too Low...Try Again..."
        return render_template('index.html', answer=answer)
    

app.run(debug=True)