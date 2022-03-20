from flask import Blueprint, render_template

blog_page = Blueprint("blog", __name__)


@blog_page.route("/")
def home_page():
    return render_template("home.html")