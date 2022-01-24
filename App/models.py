from App import db,login_manager
from datetime import date
from flask_login import UserMixin # allow to set variable is_active=True and to stay connected

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Users(db.Model,UserMixin):
    id = db.Column(db.Integer(), primary_key=True, nullable=False, unique=True)
    last_name = db.Column(db.String(length=30), nullable=False)
    first_name = db.Column(db.String(length=30), nullable=False)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    telephone_number = db.Column(db.String(length=10), nullable=True)
    is_admin = db.Column(db.Boolean(), nullable=False, default=False)

    def __repr__(self):
        return f'{self.last_name} {self.first_name}'

class Enterprise(db.Model):
    id = db.Column(db.Integer(), primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String(length=50), nullable=False, unique=True)
    place = db.Column(db.String(length=50), nullable=False)

    def __repr__(self):
        return f'{self.name} {self.place}'
  
class Candidacy(db.Model):
    id = db.Column(db.Integer(), primary_key=True, nullable=False, unique=True)
    user_id = db.Column(db.Integer(), nullable=False)
    enterprise_id = db.Column(db.Integer(), nullable=False)
    contact = db.Column(db.String(length=50), nullable=False)
    date = db.Column(db.String(), nullable=False)
    date_retry = db.Column(db.Date(), nullable=True)

    def __repr__(self):
        return f' Candidat id : {self.user_id}, Entreprise id: {self.enterprise_id}'