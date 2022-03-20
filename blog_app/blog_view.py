from unicodedata import category
from urllib import request
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import User, Category, Blog, Status
from sqlalchemy import desc
from . import db
blog_page = Blueprint("blog", __name__)

@login_required
@blog_page.route("/")
def home_page():
    blogs = Blog.query.order_by(desc(Blog.date_created)).all()
    blog_list = []
    for blog in blogs:
        username = User.query.filter_by(id=blog.created_by).first().username
        category_name = Category.query.filter_by(id=blog.category).first().category_name
        status_name = Status.query.filter_by(id=blog.status).first().status
        data = {"id" : blog.id, "title" : blog.name, "content" : blog.content, "created_by" : username, 
                "status" : status_name, "category" : category_name, "date_created" : blog.date_created}
        blog_list.append(data)
    return render_template("home_page.html", blogs=blog_list)

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

@login_required
@blog_page.route("/delete/<id>", methods=["GET", "POST"])
def delete_post(id):
    print(id)
    blog = Blog.query.filter_by(id=id).first()
    if(blog is None):
        flash("No such blog exists!", category="error")
    elif(blog.created_by == current_user.id):
        # Valid user
        db.session.delete(blog)
        db.session.commit()
        flash("Blog removed successfully!")
    else:
        flash("You are not the owner of this blog!", category="error")
    return redirect(url_for("blog.home_page"))