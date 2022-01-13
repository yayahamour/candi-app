from dataclasses import dataclass 
import sqlite3
from flask import Flask, render_template,request

app = Flask(__name__)

@dataclass
class Users : 
    last_name : str
    first_name : str 
    email : str 
    password : str 
    
    def login(self): 
        pass
    
    def logout(self): 
        pass
    
    def change_password(self): 
        pass
    
    def search_company_by_name():
        pass
    
    def search_company_by_email():
        pass
    
@dataclass
class Admin(Users):

    is_admin = True

    def search_by_apprenant():
        pass
    
    def add_promo():
        pass
    
    def add_apprenant():
        pass
    
@dataclass
class Apprenant(Users):
    promo_name : int 
    phone_number : str 
    is_admin = False

    def add_nomination():
        pass 

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
            
rudy = Apprenant("BOUREZ","Rudy","mail@mail.com","*****","DEV IA","0606060606")
rudy.modify_nomination()