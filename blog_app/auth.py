from contextlib import redirect_stderr
import imp
from unittest import result
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from .models import User
from . import db
import hashlib
import os

auth = Blueprint("auth", __name__)

# This function hashes input using md5 
def hash_password(password):
    return hashlib.md5(password.encode('utf-8')).hexdigest()

# This function hashes given input using md5 and compares it with another string
# Returns true if the hashed output is equal to the second string 
def check_hash(givenPassword, hashedPass):
    return hashlib.md5(givenPassword.encode('utf-8')).hexdigest() == hashedPass

# /auth routes to login page
@auth.route("/", methods=["GET", "POST"])
def login():
    if(request.method == "POST"):
        username = request.form.get("username")
        password = request.form.get("password")
        result = User.query.filter_by(username=username).first()
        if(result):
            # User exists; Check if password is correct 
            if(check_hash(password, result.password)):
                flash('Logged in!')
                login_user(result, remember=True)
                return redirect(url_for('blog.home_page'))
            else:
                flash('Incorrect password!', category='error')
        else:
            flash('No such user!', category='error')
    return render_template("login.html")

# /auth/signup routes to signup page and the following code is executed
@auth.route("/signup", methods=["GET", "POST"])
def sign_up():
    if(request.method == "POST"):
        username = request.form.get("username")
        result = User.query.filter_by(username=username).first()
        if(result is not None):
            # If database already has the user, then error is displayed and routed back to signup page
            flash('User \"{}\" already exist.'.format(username), category='error')
        else:
            # Generate password if user is new
            password = hashlib.md5(username.encode('utf-8')).hexdigest() 
            # Hash password for storing in DB
            hashed = hash_password(password)
            # Store in DB
            user = User(username=username, password=hashed)
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)
            flash("This is your password [Do not forget this!] :: {}".format(password))
            return redirect(url_for('blog.home_page'))

    return render_template("sign_up.html")