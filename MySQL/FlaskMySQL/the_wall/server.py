from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "ThisIsSecret!"
mysql = MySQLConnector(app,'the_wall')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    pass_confirm = request.form['pass_confirm']
    errors = False
    if len(first_name) < 1:
        errors = True
        flash("Please provide your first name")
    elif not str.isalpha(str(first_name)):
        errors = True
        flash("Please provide a valid first name")
    if len(last_name) < 1:
        errors = True
        flash("Please provide your last name")
    elif not str.isalpha(str(last_name)):
        errors = True
        flash("Please provide a valid last name") 
    if len(email) < 1:
        errors = True
        flash("Please provide your email address")
    elif not EMAIL_REGEX.match(email):
        errors = True
        flash("Please provide a valid email address")
    if len(password) < 1:
        errors = True
        flash("Please provide a password")
    elif len(password) < 8:
        errors = True
        flash("Password must be at least 8 characters in length")
    if len(pass_confirm) < 1:
        errors = True
        flash("Please confirm your password")   
    elif password != pass_confirm:
        errors = True
        flash("Passwords do not match.")
    if errors:
        return redirect('/')
    else:
        query = "SELECT * from users WHERE users.email = :email"
        data = {
                'email': email
                }
        user = mysql.query_db(query, data)
        if len(user) == 0:
            pw_hash = bcrypt.generate_password_hash(password)
            query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
            data = {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'password': pw_hash
            }
            user_id = mysql.query_db(query, data)
            flash("Thank you for registering!")
            session['user'] = user_id
            return redirect('/wall')
        else: 
            flash("Please Double Check your Information and Try Again.")
            return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    errors = False
    if len(email) < 1:
        errors = True
        flash("Please provide your email address")
    elif not EMAIL_REGEX.match(email):
        errors = True
        flash("Please provide a valid email address")
    if len(password) < 1:
        errors = True
        flash("Password cannot be empty")
    if errors:
        return redirect('/')
    else:
        query = "SELECT * from users WHERE users.email = :email"
        data = {
                'password': password,
                'email': email,
                }
        user = mysql.query_db(query, data)
        if len(user) == 0:
            flash('Email/Password Combination not recognized. Please try again or register if you are a new user.')
            return redirect('/')
        else:
            if bcrypt.check_password_hash(user[0]['password'], request.form['password']):
                flash('Welcome!')
                session['user'] = user[0]['id']
                return redirect('/wall')
            else:
                flash('Email/Password Combination not recognized. Please try again or register if you are a new user.')
                return redirect('/')

@app.route('/wall')
def wall():
    query = "SELECT messages.id, messages.content, concat(users.first_name,' ', users.last_name) AS name, date_format(messages.created_at, '%M %e, %Y') AS date from messages LEFT JOIN users ON messages.user_id = users.id"                          
    messages = mysql.query_db(query) 
    query = "SELECT comments.content, comments.message_id, concat(users.first_name,' ', users.last_name) AS name, date_format(comments.created_at, '%M %e, %Y') AS date FROM comments LEFT JOIN users ON users.id = comments.user_id"  
    comments = mysql.query_db(query) 
    return render_template('wall.html', all_messages=messages, all_comments=comments) 

@app.route('/message', methods=['POST'])
def message():
    query = "INSERT INTO messages (content, created_at, updated_at, user_id) VALUES (:content, NOW(), NOW(), :user_id)"
    data = {
            'user_id': session['user'],
            'content': request.form['message'],
            }
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/comment', methods=['POST'])
def comment():
    query = "INSERT INTO comments (content, created_at, updated_at, user_id, message_id) VALUES (:content, NOW(), NOW(), :user_id, :message_id)"
    data = {
            'user_id': session['user'],
            'content': request.form['comment'],
            'message_id': request.form['msgid']
            }
    mysql.query_db(query, data)
    return redirect('/wall')

app.run(debug=True)