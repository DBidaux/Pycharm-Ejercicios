from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wrap
import os

from wtforms.fields.html5 import EmailField

app = Flask(__name__)
app.secret_key = os.urandom(24)

#SQL
mysql = MySQL()
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "bidaux"
app.config["MYSQL_DB"] = "sslchat"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql.init_app(app)

def logged_in(f):
    @wraps(f)
    def wrap (*args, **kwargs):
        if logged_in in session:
            flash("Unauthorized, You logged in", "danger")
            return redirect(url_for("index"))
        else:
            return f(*args, **kwargs)
    return wrap

@app.route("/")
def index():
    return render_template("home.html")

class LoginForm(Form):
    username = StringField("Username", [validators.length(min=1)], render_kw = {"autofocus": True})

@app.route("/login", methods=["GET", "POST"])
@not_logged_in
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        username = form.username.data
        password_candidate = request.form["password"]

        cur = mysql.connection.cursor()

        result = cur.execute("SELECT * FROM users WHERE username =%s", [username])

        if result > 0:
            data = cur.fetchone()
            password = data["password"]
            uid = data["id"]
            name = data["name"]

        if sha256_crypt.verify(password_candidate, password):
            session["logged_in"] = True
            session ["uid"] = uid
            session["s_name"] = name
            x = "1"
            cur.execute("UPDATE users SET online=%s WHERE id=%s", (x, uid))
            flash("You are now logged in", "success")

            return redirect(url_for("index"))
        else:
            flash("Incorrect password", "danger")
            return render_template("login.html", form=form)
    else:
        flash("Username not found", "danger")
        cur.close()
        return render_template("login.html", form=form)

    return render_template("login.html", form=form)

103