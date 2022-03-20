from unicodedata import category
from urllib import request
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import User, Category, Blog, Status
from . import db
blog_page = Blueprint("blog", __name__)

@login_required
@blog_page.route("/")
def home_page():
    return render_template("home_page.html")

@login_required
@blog_page.route("/create", methods=["GET", "POST"])
def create_page():
    categories = Category.query.all()
    statuses = Status.query.all()
    if(request.method == "POST"):
        categoryId = request.form.get("Category")
        statusId = request.form.get("Status")
        title = request.form.get("title")
        content = request.form.get("content")
        new_blog = Blog(name=title, status=statusId, category=categoryId, content=content, created_by=current_user.id)
        db.session.add(new_blog)
        db.session.commit()
        flash("Created new blog!")
    return render_template("create_blog.html", categories=categories, statuses=statuses)