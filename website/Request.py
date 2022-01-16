from os import name
import sqlite3
from . import db 
from .models import Entreprise, Candidature, User
from sqlalchemy.sql import select 


class Request():
    
    def get_db_connection(self):
        return(sqlite3.connect('website/DB/base_test.db'))
     
    def request_nomination_by_id(self, id):
        connection = self.get_db_connection()
        request = "SELECT E.name, E.place, C.contact, C.date_nomination, C.status FROM Candidature as C Join User as U ON U.id = C.user_id JOIN Entreprise as E ON E.id = C.enterprise_id WHERE U.id = "+ str(id)
        result = connection.execute(request).fetchall()
        connection.close()
        return result

    def request_nomination_by_entreprise_name(self, entreprise_name):
        connection = self.get_db_connection()
        request = "SELECT U.last_name, U.first_name, E.place, C.contact FROM Candidature as C Join User as U ON U.id = C.user_id JOIN Entreprise as E ON E.id = C.enterprise_id WHERE E.name = '" + entreprise_name +"'"
        result = connection.execute(request).fetchall()
        connection.close()
        return result
            
    def request_nomination_by_lastname(self, lastname):
        connection = self.get_db_connection()
        request = "SELECT Entreprise.name, Entreprise.place, Candidature.contact FROM Candidature, Entreprise WHERE (SELECT id from User WHERE LOWER(last_name) = '"+ lastname.lower() +"') = Candidature.user_id AND Candidature.enterprise_id = Entreprise.id"
        result = connection.execute(request).fetchall()
        connection.close()
        return result
    
    def request_nomination_by_firstname(self, first_name):
        connection = self.get_db_connection()
        request = "SELECT Entreprise.name, Entreprise.place, Candidature.contact FROM Candidature, Entreprise WHERE (SELECT id from User WHERE LOWER(first_name) = '"+ first_name.lower() +"') = Candidature.user_id AND Candidature.enterprise_id = Entreprise.id"
        result = connection.execute(request).fetchall()
        connection.close()
        return result

    def request_nomination_by_firstname_lastname(self, first_name, lastname):
        connection = self.get_db_connection()
        request = "SELECT Entreprise.name, Entreprise.place, Candidature.contact FROM Candidature, Entreprise WHERE (SELECT id from User WHERE LOWER(last_name) = '"+ lastname.lower() + "' AND LOWER(first_name) = '"+ first_name.lower() +"') = Candidature.user_id AND Candidature.enterprise_id = Entreprise.id"
        result = connection.execute(request).fetchall()
        connection.close()
        return result
    
    def request_all_nomination(self):
        connection = self.get_db_connection()
        request = "SELECT User.last_name, User.first_name, Entreprise.name, Entreprise.place, Candidature.contact, Candidature.date_nomination, Candidature.status FROM User, Candidature, Entreprise WHERE User.id = Candidature.user_id AND Candidature.enterprise_id = Entreprise.id"
        result = connection.execute(request).fetchall()
        connection.close()
        return result
    
    def table_candidature():
        # Jointure a revoir ne fonctionne pas bien. 
        conn = db.engine.connect()
        test = db.session.query(Entreprise.name, Entreprise.place, Candidature.contact, Candidature.date, Candidature.status, User.first_name, User.last_name).all()
        test2 = select(Entreprise.name, Entreprise.place, Candidature.contact, Candidature.date, Candidature.status, User.first_name, User.last_name, User.id).where( User.id == Candidature.id)
        result = conn.execute(test2)
        return result
    
    def table_candidature2():
        # test 
        conn = db.engine.connect()
        target = select(User.last_name, User.first_name, Entreprise.name, Entreprise.place, Candidature.contact, Candidature.date, Candidature.status).where( User.id == Candidature.user_id , Candidature.enterprise_id == Entreprise.id)
        result = conn.execute(target)
        return result 
    
    
# ----------------------------------------------------------------> Note
# db.session.query(Entreprise).all()
# Revient exactement au meme que Entreprise.query.all() -- 
# A revoir pour la différence ? 
        

# # Pour voir dans les tables : 
#     user = User.query.all()
#     for use in user :
#         print('Entreprise  : ' , use.name)
        
#     user = User.query.all()
#     for use in user:
#         print('Users : ', use.last_name)
    
    # Je commence une migration avec des requete myslqlalchemy.  

request = Request()

# print("request nomination 1")
# RESULT = request.request_nomination_by_id(1)
# for i in RESULT:
#     print(i)
    

# print("request nomination Rudy")
# RESULT = request.request_nomination_by_firstname("Rudy")
# for i in RESULT:
#     print(i)
    
# print("request nomination Bourez")
# RESULT = request.request_nomination_by_lastname("Bourez")
# for i in RESULT:
#     print(i)

# print("request nomination RUDy Bourez")
# RESULT = request.request_nomination_by_firstname_lastname("RUDY", "Bourez")
# for i in RESULT:
#     print(i)
    
# print("request all nomination")
# RESULT = request.request_all_nomination()
# for i in RESULT:
#     print(i)
    
# print("request nomination Urluberlu")
# RESULT = request.request_nomination_by_entreprise_name("Urluberlu")
# for i in RESULT:
#     print(i)