from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config["DEBUG"] = True   # display runtime errors in the browser

def error(string):
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
    pass_1, a string
    pass_2, a string
    """
    if pass_1 == pass_2:
        return error(pass_1)
    else:
        return False

def verify_email(email):
    """
    checks if email is a string with a single @ and a single .(dot)
    ```
    email, a string
    """
    if '@' in email and '.' in email:
        return error(email)
    else:
        return True

@app.route("/", methods=["GET"])
def base():
    return render_template("signup.html")

@app.route("/verification", methods=["POST"])
def verification():
    """
    checks if username, password and email are legit.
    ```
    username, must be 3-20 char long with no spaces
    password, must be 3-20 char long with no spaces
    email, **optional, but must have a @ and no spaces
    """ 
    username = ""
    password = ""
    email = ""
    username_error = False
    password_error = False
    email_error = False

    if not error(request.form['typed_username']):
        username = request.form['typed_username']
    else:
        username_error = True

    if not password_verification(request.form['typed_password'],request.form['verify_password']):
        password = request.form['typed_password']

    if request.form['typed_email']:
        email_error = verify_email(request.form['typed_email'])
        if not email_error:
          email = request.form['typed_email']

    if not username_error and not password_error and not email_error:
        return render_template("welcome.html",html_username=username)
    else:
        return render_template("signup.html",html_username=username,html_email=email,html_username_error=username_error,html_password_error=password_error,html_password_verification_error=password_verification(request.form['typed_password'],request.form['verify_password']),html_email_error=email_error)


app.run()