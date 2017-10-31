from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "this is a secret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    location = request.form['location']
    comment = request.form['comment']
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
    else:
        flash("Success! Thank you, {}".format(name))
    if len(comment) < 1:
        flash("Comment cannot be empty!")
    elif len(comment) > 120:
        flash("Comment must be less than 120 characters")
    else: 
        flash("Thank you, your comment has been recorded.")
    return redirect('/')

app.run(debug=True)