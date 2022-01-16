from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    last_name = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    tel_number = db.Column(db.String(10))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    is_admin = db.Column(db.Boolean, unique=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())


class Entreprise(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(150))
    place = db.Column(db.String(150))
    contact = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone=True), default=func.now())


class Candidature(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    enterprise_id = db.Column(db.String(10000), db.ForeignKey('entreprise.id'), nullable=False)
    contact = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    status = db.Column(db.String(50))
    



    
    
