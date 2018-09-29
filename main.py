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

def error_check(string):
    """
    checks is a string has any spaces in it and if it is within 3-20 chars long
    ```
    string, a string
    """
    if ' ' in string and (len(string) > 3 and len(string) < 20):
        return True
    else:
        return False

def password_verification(pass_1,pass_2):
    """
    checks if password value matches verify password value
    ```
    pass1, a string
    pass2, a string
    """
    if pass1 == pass2:
        return True
    else:
        return False

def verify_email(email):
    """
    checks if email is a string with a single @ and a single .(dot)
    ```
    email, a string
    """
    if '@' in email and '.' in email:
        return error_check(email)
    else:
        return True

@app.route("/", methods=["GET"])
def base():
    return render_template("signup.html", html_username=username, html_email=email)

@app.route("/verification", methods=["POST"])
def verification():
    """
    checks if username, password and email are legit.
    ```
    username, must be 3-20 char long with no spaces
    password, must be 3-20 char long with no spaces
    email, **optional, but must have a @ and no spaces
    """ 
    username_error = error_check(request.form['typed_username'])
    if username_error == False:
        username = request.form['typed_username']

    password_error = error_check(request.form['typed_password'])
    if password_error == False and password_verification(request.form['typed_password'],request.form['verify_password']):
        password = request.form['typed_password']

    if request.form['typed_email']:
        email_error = verify_email(request.for['typed_email'])
    if email_error == False:
        email = request.form['typed_email']

    if not username_error and not password_error and not email_error:
        return render_template("welcome.html",html_username=username)
    else:
        return render_template("signup.html", html_username=username, html_email=email)


app.run()