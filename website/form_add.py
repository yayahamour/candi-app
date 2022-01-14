from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    entreprise = StringField('Entreprise', validators=[DataRequired()])
    lieu = StringField('Lieu', validators=[DataRequired()])
    contact = StringField('Contact', validators=[DataRequired()])
    # date = StringField('Date de candidature', validators=[DataRequired()])
    # date_de_relance = StringField('Date de relance')
    # statut = StringField('Statut de la candidature', validators=[DataRequired()])
    submit = SubmitField('Ajouter')

