from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True   # display runtime errors in the browser

@app.route('/', methods="")
def base():
    return render_template("signup.html")

@app.route('/signup-verification', methods='POST')
def signup_verification():
    



app.run()