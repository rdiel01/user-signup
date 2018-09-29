from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config["DEBUG"] = True   # display runtime errors in the browser

username = ""
password = ""
email = ""
invalid=[' ','/','\\','\'','"','@']
username_error = False
password_error = False
email_error = False

@app.route("/", methods=["GET"])
def base():
    return render_template("signup.html", html_username=username, html_email=email)

@app.route("/verification", methods=["POST"])
def verification():
    if ' ' is in request.form['typed_username'] and (len(request.form['typed_username']) >= 3 and len(request.form['typed_username']) <= 20:
        username_error = True
    else:
        username_error = False
        username = request.form['typed_username']

    password = request.form['typed_password']
    email = request.form['typed_email']
    if not username_error and not password_error and not email_error:
        return render_template("welcome.html",html_username=username)


app.run()