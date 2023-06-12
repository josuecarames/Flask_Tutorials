###################################

from flask import Flask, render_template, redirect, url_for, request

###################################

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
    
# Route for handling the login page logic
# Current username and pw that are accepted are both "admin"

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

###################################

#Add welcome.html route
    
@app.route('/welcome')
def welcome():
    error = None
    return render_template('/welcome.html', error = error)