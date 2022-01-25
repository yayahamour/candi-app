from flask_wtf import FlaskForm
from wtforms import PasswordField,EmailField,SubmitField,StringField, SelectField
from wtforms.validators import Length,DataRequired,Email,EqualTo,ValidationError
from .models import Users

class Login(FlaskForm):

    email = EmailField(label="Adresse mail:", validators = [DataRequired()])
    password = PasswordField(label="Mot de passe:", validators = [DataRequired()])
    submit = SubmitField(label="Se connecter")


class AddCandidacy(FlaskForm):
    name = StringField(label='Entreprise', validators=[DataRequired()])
    place = StringField(label='Lieu', validators=[DataRequired()])
    contact = StringField(label='Contact', validators=[DataRequired()])
    submit = SubmitField(label='Ajouter')

class ModifyProfile(FlaskForm):
    
    email = EmailField(label="Adresse mail:", validators = [DataRequired()])
    current_password = PasswordField(label="Mot de passe actuel:", validators = [DataRequired()])
    new_password = PasswordField(label="Nouveau mot de passe:", validators = [DataRequired()])
    submit = SubmitField(label="Valider")

class ModifyCandidacy(FlaskForm):
  
    contact = StringField(label='Contact', validators=[DataRequired()])
    status = SelectField(label='Status', choices=['En cours', 'Validée', 'Refusée'], validate_choice=True, coerce=str)

    submit = SubmitField(label="Valider")