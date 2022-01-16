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


@views.route('/board-all', methods = ['GET'])
@login_required
def board_admin():
    return render_template('board-all.html', title = ["Nom", "Prenom","Nom Entreprise", "Ville","Contact", "Date", "Status",""],name_table = "Candidat",db=Request.table_candidature_admin())

    
@views.route('/formulaire', methods=['GET','POST'])
@login_required
def formulaire():
    
    
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

@views.route('/formulaire-add2', methods=['GET','POST'])
@login_required
def formulaire_nomination():


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




# def modify_nomination(self):
#     enterprise = 1 # Enterprise_id obtained from HTML attribute
#     conn = sqlite3.connect('website/DB/base_test.db')
#     my_modification = conn.cursor()
#     my_modification.execute("""SELECT name, place, contact
#     FROM Candidature AS c
#     JOIN User AS u ON u.id=c.user_id
#     JOIN Entreprise AS e ON e.id=c.enterprise_id
#     WHERE u.first_name = ? AND e.id = ?""", (self.first_name,enterprise,))
#     row = my_modification.fetchone()
#     @users.route('/Xformulaire', methods=('GET','POST'))
#     def add_formulaire():
#         if request.method == "POST":
#             entreprise = request.form.get("Entreprise")
#             lieu = request.form.get("Lieu")
#             contact = request.form.get("Contact")
#             date = request.form.get("Date")
#             date_de_relance = request.form.get("Date de relance")
#             statut = request.form.get("Statut")
#         # Ajouter le update sql 
#         return render_template('Formulaire.html',row=row, liste=["Entreprise","Lieu","Contact","Date","Date de relance","Statut"])




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