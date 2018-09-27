from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True   # display runtime errors in the browser

@app.route('/')
def base():
    return render_template("signup.html")

app.run()