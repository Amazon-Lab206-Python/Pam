from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def hello():
    return render_template('hello.html')

@app.route('/accounts')
def accounts():
    return render_template('accounts.html')

app.run(debug=True)