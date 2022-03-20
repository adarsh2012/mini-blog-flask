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
    setup_db_data(app)
    #Login
    login_manager = LoginManager()
    login_manager.login_view =  "auth.login"
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


def setup_db_data(app):
    with app.app_context():
        from .models import Category, Status
        # Adding pre-existing data (workaround; technically should be able to add this from website)
        categories = ["Buisness", "Science", "Social", "Others"]
        statuses = ["active", "in-active"]
        for category in categories:
            result = Category.query.filter_by(category_name=category).first()
            if(result is None):
                new_category = Category(category_name=category)
                db.session.add(new_category)
                db.session.commit()
        for status in statuses:
            result = Status.query.filter_by(status=status).first()
            if(result is None):
                new_status = Status(status=status)
                db.session.add(new_status)
                db.session.commit()