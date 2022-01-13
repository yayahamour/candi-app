from os import name
import re
import flask
from mysql.connector import ERROR_NO_CEXT, connect, Error, connection

from getpass import getpass
from mysql.connector import connect, Error

class Request():
    
    def __init__(self) -> None:
        self.db = connect(
        host="localhost",
        user="root",
        password="08.02.98.Yanis",
        database ="Candidature_simplon"
    )  
    
    def request_nomination_by_entreprise_name(self, entreprise_name):
        request = "SELECT U.last_name, U.first_name, E.place, C.contact FROM Candidature as C Join User as U ON U.id = C.user_id JOIN Entreprise as E ON E.id = C.enterprise_id WHERE E.name = '" + entreprise_name +"'"
        cur = self.db.cursor()
        cur.execute(request)
        for row in cur.fetchall():
            print(row)
            
    def request_nomination_by_lastname(self, lastname):
        request = "SELECT Entreprise.name, Entreprise.place, Candidature.contact FROM Candidature, Entreprise WHERE (SELECT id from User WHERE LOWER(last_name) = '"+ lastname.lower() +"') = Candidature.user_id AND Candidature.enterprise_id = Entreprise.id"
        cur = self.db.cursor()
        cur.execute(request)
        for row in cur.fetchall():
            print(row)
    
    def request_nomination_by_firstname(self, first_name):
        request = "SELECT Entreprise.name, Entreprise.place, Candidature.contact FROM Candidature, Entreprise WHERE (SELECT id from User WHERE LOWER(first_name) = '"+ first_name.lower() +"') = Candidature.user_id AND Candidature.enterprise_id = Entreprise.id"
        cur = self.db.cursor()
        cur.execute(request)
        for row in cur.fetchall():
            print(row)

    def request_nomination_by_firstname_lastname(self, first_name, lastname):
        request = "SELECT Entreprise.name, Entreprise.place, Candidature.contact FROM Candidature, Entreprise WHERE (SELECT id from User WHERE LOWER(last_name) = '"+ lastname.lower() + "' AND LOWER(first_name) = '"+ first_name.lower() +"') = Candidature.user_id AND Candidature.enterprise_id = Entreprise.id"
        cur = self.db.cursor()
        cur.execute(request)
        for row in cur.fetchall():
            print(row)
    
    def request_all_nomination(self):
        request = "SELECT User.last_name, User.first_name, Entreprise.name, Entreprise.place, Candidature.contact FROM User, Candidature, Entreprise WHERE User.id = Candidature.user_id AND Candidature.enterprise_id = Entreprise.id"
        cur = self.db.cursor()
        cur.execute(request)
        for row in cur.fetchall():
            print(row)

request = Request()
print("request nomination Rudy")
request.request_nomination_by_firstname("Rudy")
print("request nomination Bourez")
request.request_nomination_by_lastname("Bourez")
print("request nomination RUDy Bourez")
request.request_nomination_by_firstname_lastname("RUDY", "Bourez")
print("request all nomination")
request.request_all_nomination()
print("request nomination Urluberlu")
request.request_nomination_by_entreprise_name("Urluberlu")