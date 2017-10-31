from flask import Flask, render_template, request, session, redirect 
app = Flask(__name__)
app.secret_key = "this is so secret"

@app.route('/')
def index():
    try:
        session['counter']
    except:
        session['counter'] = 0

    session['counter'] += 1

    return render_template('index.html')

app.run(debug=True)