import flask
from flask_sqlalchemy import SQLAlchemy
import os
import flask_login



def create_app():
    app = flask.Flask(__name__)
    app.config["SECRET_KEY"] = "adsd"

    from .auth import auth
    from .blog_view import blog_page
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(blog_page, url_prefix="/blog")
    return app