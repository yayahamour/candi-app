from flask import Blueprint, render_template, request, flash, redirect, url_for
from website.Request import Request as Req
from flask_login import login_required, current_user
from datetime import date
from . import models 
from .models import Entreprise, User, Candidature
from sqlalchemy import insert , select , MetaData, Table , MetaData, create_engine, inspect
from . import db , DB_NAME
from .Request import Request

# from .models import Candidature

views = Blueprint('views', __name__)


# Home 
@views.route('/')
def home():
    render_template('base.html', boolean = True, current_user = current_user)
    return redirect(url_for('auth.login'))


# Dashboard users
@views.route('/board', methods=['GET'])
@login_required
def board():

    return render_template('board.html', title = ["Nom", "Prenom","Nom Entreprise", "Ville","Contact", "Date", "Status",""],name_table = "Apprenant Dashboard",db=Request.table_candidature_user() , Request = Request)


# Dashboard admin
@views.route('/board-admin', methods = ['GET'])
@login_required
def board_admin():
    return render_template('board-all.html', title = ["Nom", "Prenom","Nom Entreprise", "Ville","Contact", "Date", "Status",""],name_table = "Admin - Dashboard",db=Request.table_candidature_admin())




# Form to add a new nomination (Candidature)
@views.route('/formulaire-candidature', methods=['GET','POST'])
@login_required
def nomination_add():



    if request.method == "POST":
        
        contact = request.form.get("contact")
        status = request.form.get("status")
        entreprise_choice = request.form.get("monselect")
        if not entreprise_choice :
            flash('Veuillez choisir une entreprise', category='error')
        elif entreprise_choice == "Aucun":
            flash('Veuillez choisir une entreprise', category='error')
        else:
            choice_2 = db.session.query(Entreprise).filter(Entreprise.name == entreprise_choice)
            entrepriseID = ""
            for i in choice_2 :
                entrepriseID = i.id 
            new_candidature = Candidature(contact=contact, status=status , enterprise_id = entrepriseID,  user_id = current_user.id)
            db.session.add(new_candidature)
            db.session.commit()
            flash('Nouvelle Candidature ajouté ', category='succes')
            return redirect(url_for('views.board'))
    return render_template('form_add2.html',  entreprises = Entreprise.query.all())


# Form to Add an Enterprise
@views.route('/formulaire-entreprise', methods=['GET','POST'])
@login_required
def enterprise_add():
    
    
    if request.method == "POST":
        
        entreprise = request.form.get("entreprise")
        lieu = request.form.get("adresse")
        
        filter = Entreprise.query.filter_by(name=entreprise).first()
        if filter :
            flash('Cette entreprise a déja été ajouté', category='error')
        else:
            
            new_entreprise = Entreprise(name=entreprise,place=lieu)
            flash('Nouvelle entreprise ajouté', category='succes')
            
            db.session.add(new_entreprise)
            db.session.commit()
            
            return redirect(url_for('views.board'))
    return render_template('form_add.html', current_user=current_user, entreprises = Entreprise.query.all())




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