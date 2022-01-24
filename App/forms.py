from flask_wtf import FlaskForm
from wtforms import PasswordField,EmailField,SubmitField
from wtforms.validators import Length,DataRequired,Email,EqualTo,ValidationError
from .models import Users

class Login(FlaskForm):

    email = EmailField(label="Adresse mail:", validators = [DataRequired()])
    password = PasswordField(label="Mot de passe:", validators = [DataRequired()])
    submit = SubmitField(label="Se connecter")