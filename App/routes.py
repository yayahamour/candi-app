from flask import render_template, redirect, url_for, flash, request
from App import db, app
from datetime import date
from App.request import Request
from .models import Users, Enterprise, Candidacy
from .forms import Login, AddCandidacy, ModifyCandidacy, ModifyProfile
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
    if (current_user.is_admin == True):
        return render_template('board.html', title = ["Nom", "Prenom","Nom Entreprise", "Ville","Contact", "Date", "Status"],User=req.request_all_nomination())
    else:
        return render_template('board.html', title = ["ID","Nom Entreprise", "Ville","Contact", "Date", "Status",""],User=req.request_nomination_by_id(current_user.id))

@app.route('/logout')
def logout_page():
    logout_user()
    flash('Vous êtes correctement déconnecté',category="success")
    return redirect(url_for('home_page'))

@app.route('/candidature', methods= ['GET', 'POST'])
def add_candidature():
    form = AddCandidacy()
    date_candidacy = date.today().strftime("%d-%m-%Y")
    print(date_candidacy)
    print(type(date_candidacy))
    if form.validate_on_submit():
        enterprise = Enterprise.query.filter_by(name=form.name.data, place=form.place.data).first()
        if enterprise:
            pass
        else:
            enterprise1 = Enterprise(name=form.name.data, place=form.place.data)
            db.session.add(enterprise1)
            db.session.commit()
        enterprise_ID = Enterprise.query.filter_by(name=form.name.data, place=form.place.data).first().id
        print(enterprise_ID)
        new_candidature = Candidacy(contact=form.contact.data, enterprise_id = enterprise_ID,  user_id = current_user.id, date=date_candidacy)
        db.session.add(new_candidature)
        db.session.commit()
        flash('Nouvelle Candidature ajouté ', category='success')
        return redirect(url_for('board_page'))
    return render_template('add_candidacy.html', form=form)

@app.route('/modify_profile', methods=['GET', 'POST'])
@login_required
def modify_profile():
    form = ModifyProfile()
    if form.validate_on_submit():
        if current_user.email_address == form.email.data and current_user.password_hash == form.current_password.data:
            current_user.password_hash = form.new_password.data
            db.session.add(current_user)
            db.session.commit()

            flash(f"Votre mot de passe a été modifié",category="success")
            return redirect(url_for('board_page'))
        else:
            flash('Adresse email ou mot de passe invalide',category="danger")
    return render_template('modify_profile.html',form=form)

@app.route('/modify_candidacy', methods=['GET', 'POST'])
@login_required
def modify_candidacy():
    form = ModifyCandidacy()
    candidacy_id = request.args.get('id')
    candidacy = Candidacy.query.filter_by(id = candidacy_id).first()

    if form.validate_on_submit():
        
        if candidacy:
            candidacy.contact = form.contact.data
            candidacy.status = form.status.data
            db.session.commit()

            flash(f"La candidature a bien été modifié",category="success")
            return redirect(url_for('board_page'))
        else:
            flash('Something goes wrong',category="danger")
    return render_template('modify_candidacy.html', form=form , contact = candidacy.contact)
    
@app.route('/delete_candidacy')
def delete_candidacy():
    print("bonjour")
    candidacy_id = request.args.get('id')
    Candidacy.query.filter_by(id=candidacy_id).delete()
    db.session.commit()
    flash("Candidature supprimé avec succés",category="success")
    return redirect(url_for('board_page'))
