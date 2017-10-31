from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if len(request.form['first_name']) < 1:
        flash("Please provide your first name")
    elif not str.isalpha(str(request.form['first_name'])):
        flash("Please provide a valid first name")
    if len(request.form['last_name']) < 1:
        flash("Please provide your last name")
    elif not str.isalpha(str(request.form['last_name'])):
        flash("Please provide a valid last name") 
    if len(request.form['email']) < 1:
        flash("Please provide your email address")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Please provide a valid email address")
    if len(request.form['password']) < 1:
        flash("Please provide a password")
    elif len(request.form['password']) < 8:
        flash("Password must be at least 8 characters in length")
    if len(request.form['confirm_pass']) < 1:
        flash("Please confirm your password")   
    if request.form['password'] != request.form['confirm_pass']:
        flash("Passwords do not match.")
    else:
        flash("Success! Thank you for submitting your information") 
    return redirect('/') 
app.run(debug=True)