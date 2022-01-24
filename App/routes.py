from flask import render_template, redirect,url_for,flash
from App import db, app
from App.request import Request
from .models import Users
from .forms import Login
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = Login()
    if form.validate_on_submit():
        user = Users.query.filter_by(email_address=form.email.data).first()
        if user and user.password_hash == form.password.data:
            login_user(user)
            flash(f"Vous êtes connecté en tant que : {user.first_name} {user.last_name}",category="success")
            return redirect(url_for('board_page'))
        else:
            flash('Adresse email ou mot de passe invalide',category="danger")
    return render_template('login.html',form=form)

@app.route('/board', methods=['GET','POST'])
@login_required
def board_page():
    req = Request()
    if (current_user.is_admin == "True"):
        return render_template('board.html', title = ["Nom", "Prenom","Nom Entreprise", "Ville","Contact", "Date", "Status",""],User=req.request_all_nomination())
    else:
        return render_template('board.html', title = ["Nom Entreprise", "Ville","Contact", "Date", "Status",""],User=req.request_nomination_by_id(current_user.id))

@app.route('/logout')
def logout_page():
    logout_user()
    flash('Vous êtes correctement déconnecté',category="success")
    return redirect(url_for('home_page'))