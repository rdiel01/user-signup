from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config["DEBUG"] = True   # display runtime errors in the browser

username = ""
password = ""
email = ""

@app.route("/", methods=["GET"])
def base():
    return render_template("signup.html", html_username=username, html_email=email)

@app.route("/verification", methods=["POST"])
def verification():
    username = request.form['typed_username']
    password = request.form['typed_password']
    email = request.form['typed_email']
    pass


app.run()