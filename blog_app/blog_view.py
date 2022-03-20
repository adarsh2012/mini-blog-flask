from urllib import request
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Category, Blog, Status
blog_page = Blueprint("blog", __name__)


@blog_page.route("/")
def home_page():
    return render_template("home_page.html")

@blog_page.route("/create", methods=["GET", "POST"])
def create_page():
    categories = Category.query.all()
    statuses = Status.query.all()
    if(request.method == "POST"):
        categoryId = request.form.get("Category")
        statusId = request.form.get("Status")
        title = request.form.get("title")
        content = request.form.get("content")
    return render_template("create_blog.html", categories=categories, statuses=statuses)