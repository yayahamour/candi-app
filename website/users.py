from dataclasses import dataclass
import sqlite3
from flask import Flask, render_template,request, flash, redirect, url_for
from website.form_add import LoginForm
from datetime import date

app = Flask(__name__)
@dataclass
class Users :

    id : int
    last_name : str
    first_name : str 
    email : str 
    password : str 
    
    def change_password(self): 
        pass
    
    def search_company_by_name():
        pass
    
    def search_company_by_email():
        pass
    
@dataclass
class Admin(Users):

    is_admin :bool = True
    is_active : bool = False 

    def search_by_apprenant():
        pass
    
    def add_promo():
        pass
    
    def add_apprenant():
        pass
    
@dataclass
class Apprenant(Users):

    phone_number :str 
    is_admin :bool = False
    is_active : bool = False 

    def add_nomination():
        form_add = LoginForm()
        if form_add.validate_on_submit():
            entreprise = request.form["Entreprise"]
            lieu = request.form["Lieu"]
            contact = request.form["Contact"]
            my_date = date.today().strftime("%b-%d-%Y")
            status = "En cours"

            c = sqlite3.connect('website/DB/base_test.db')
            nomination = c.cursor()
            # check if entreprise is in Entreprise table
            is_entreprise = nomination.execute("SELECT id, name FROM Entreprise WHERE name = ?", (entreprise,))
            if not is_entreprise :
                # add new enterprise in Entreprise table
                nomination.execute("INSERT INTO Entreprise (name, lieu) VALUES (?,?)", (entreprise, lieu,))
                new_enterprise_id = ("SELECT MAX(id) FROM Entreprise")
                # add new nomination in Candidature table
                nomination.execute("INSERT INTO Candidature (user_id, enterprise_id, contact, date_nomination, status) VALUES (?, ?, ?)", (self.id, new_enterprise_id, contact, my_date,status,))
            else :
                enterprise_id = is_entreprise[0]
                nomination.execute("INSERT INTO Candidature (user_id, enterprise_id, contact, date_nomination)",(self.id, enterprise_id, contact, my_date,status,))
            c.commit()

            flash('Candidature ajoutée pour {}'.format(form_add.enterprise.data))
            
            return redirect(url_for('board'))
        return render_template('board.html', form_add=form_add)
     
     

    def modify_nomination(self):
        enterprise = 1 # Enterprise_id obtained from HTML attribute
        conn = sqlite3.connect('website/DB/base_test.db')
        my_modification = conn.cursor()
        my_modification.execute("""SELECT name, place, contact
        FROM Candidature AS c
        JOIN User AS u ON u.id=c.user_id
        JOIN Entreprise AS e ON e.id=c.enterprise_id
        WHERE u.first_name = ? AND e.id = ?""", (self.first_name,enterprise,))
        row = my_modification.fetchone()
        @app.route('/', methods=('GET','POST'))
        def add_formulaire():
            if request.method == "POST":
                entreprise = request.form.get("Entreprise")
                lieu = request.form.get("Lieu")
                contact = request.form.get("Contact")
                date = request.form.get("Date")
                date_de_relance = request.form.get("Date de relance")
                statut = request.form.get("Statut")
            return render_template('Formulaire.html',row=row, liste=["Entreprise","Lieu","Contact","Date","Date de relance","Statut"])
