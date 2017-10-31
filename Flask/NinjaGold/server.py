from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "this is so secret"
import random

@app.route('/')
def index():
    try:
        session['gold']
    except:
        session['gold'] = 0
    return render_template('index.html')

@app.route('/process_money')
def money():
    if request.form['building'] == 'farm':
        session['gold'] += random.randint(10,21)
