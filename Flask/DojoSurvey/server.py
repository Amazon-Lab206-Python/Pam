from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    location = request.form['location']
    comment = request.form['comment']
    return render_template('result.html', name=name, location=location, comment=comment)

@app.route('/')
def index():
    return render_template('index.html')


app.run(debug=True)