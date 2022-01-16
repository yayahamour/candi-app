from flask import Blueprint, render_template, request, flash, redirect, url_for
from website.Request import Request as Req
from flask_login import login_required, current_user
import sqlite3
from datetime import date
from . import models 
from .models import Entreprise, User, Candidature
from sqlalchemy import insert , select , MetaData, Table , MetaData, create_engine, inspect
from . import db , DB_NAME
from .Request import Request

# from .models import Candidature

views = Blueprint('views', __name__)

@views.route('/')
def home():
    render_template('base.html', boolean = True, current_user = current_user)
    return redirect(url_for('auth.login'))


@views.route('/board', methods=['GET'])
@login_required
def board():

    return render_template('board.html', title = ["Nom", "Prenom","Nom Entreprise", "Ville","Contact", "Date", "Status",""],name_table = "Candidat",db=Request.table_candidature_user())


@views.route('/board-admin', methods = ['GET'])
@login_required
def board_admin():
    return render_template('board-all.html', title = ["Nom", "Prenom","Nom Entreprise", "Ville","Contact", "Date", "Status",""],name_table = "Candidat",db=Request.table_candidature_admin())

    
@views.route('/formulaire-entreprise', methods=['GET','POST'])
@login_required
def enterprise_add():
    
    
    if request.method == "POST":
        
        entreprise = request.form.get("entreprise")
        lieu = request.form.get("adresse")
        contact = request.form.get("contact")
        
        filter = Entreprise.query.filter_by(name=entreprise).first()
        if filter :
            flash('Cette entreprise a déja été ajouté', category='error')
        else:
            
            new_entreprise = Entreprise(name=entreprise,place=lieu, contact=contact)
            flash('Nouvelle entreprise ajouté', category='succes')
            
            db.session.add(new_entreprise)
            db.session.commit()
            
            return redirect(url_for('views.board'))
    return render_template('form_add.html', current_user=current_user, entreprises = Entreprise.query.all())

@views.route('/formulaire-candidature', methods=['GET','POST'])
@login_required
def nomination_add():


    if request.method == "POST":
        
        entreprise = request.form.get("entreprise")
        ville = request.form.get("ville")
        contact = request.form.get("contact")
        status = request.form.get("status")
        entreprise_choice = request.form.get("monselect")
        filter = Entreprise.query.filter_by(name=entreprise).first()
        filter_2 = Entreprise.query.filter_by(contact=contact).first()
        # Ajouter le filtre 2 pour choisir le contact quand existe 
        # Ajouter if choice == 'AUTRE ou AUCUN' pour ajouté une candidature ? 
        if filter :
            flash('Cette entreprise a déja été ajouté, attendre l\'implémentation du insert', category='error')
            # db.engine.Candidature.insert((entreprise_name => where entreprise_name == Candidature ), contact=contact, status = status).where()
        else:
            

            new_entreprise = Entreprise(name = entreprise ,place = ville, contact=contact )
            new_candidature = Candidature(contact=contact, status=status , enterprise_id = 1, user_id = current_user.id)
            flash('Nouvelle Candidature ajouté ', category='succes')
            
            db.session.add(new_entreprise)
            db.session.add(new_candidature)
            db.session.commit()
            
            return redirect(url_for('views.board'))

    return render_template('form_add2.html',  entreprises = Entreprise.query.all())



# ------------------------------------------------------------------------- > Note 
# db.session.query(Entreprise).all()
# Revient exactement au meme que Entreprise.query.all() -- 
# A revoir pour la différence ? 


# # Pour voir dans les tables : 
#     user = Entreprise.query.all()
#     for use in user :
#         print('Entreprise  : ' , use.name)
        
#     user = User.query.all()
#     for use in user:
#         print('Users : ', use.last_name)