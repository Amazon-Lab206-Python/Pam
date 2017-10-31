from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "super secret"

@app.route('/')
def index():
    if not counter in session:
        session['counter'] = 0
    return render_template('index.html')

@app.route('/info', methods=["POST"])
def info():
    session['counter'] += 1
    session['name'] = request.form['name']
    print session['name']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')

app.run(debug=True)