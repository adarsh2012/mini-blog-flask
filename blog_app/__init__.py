import flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = flask.Flask(__name__)
    app.config["SECRET_KEY"] = "adsd"
    #DB configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@127.0.0.1:3306/mini_blog"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    from .models import User
    db.init_app(app)
    db.create_all(app=app)
    #Login
    login_manager = LoginManager()
    login_manager.login_view =  "auth.view"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    #Routing
    from .auth import auth  
    from .blog_view import blog_page
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(blog_page, url_prefix="/blog")
    return app