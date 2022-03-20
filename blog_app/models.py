from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func



class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())


class Blog(db.Model):
    __tablename__ = 'blog'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), unique=True)
    body_text = db.Column(db.Text)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())