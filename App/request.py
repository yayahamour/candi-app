from os import name
import re
import flask
import sqlite3

class Request():
    
    def get_db_connection(self):
        return(sqlite3.connect('App/candidature.db'))
     
    def request_nomination_by_id(self, id):
        connection = self.get_db_connection()
        request = "SELECT E.name, E.place, C.contact, C.date FROM Candidacy as C Join Users as U ON U.id = C.user_id JOIN Enterprise as E ON E.id = C.enterprise_id WHERE U.id = "+ str(id)
        result = connection.execute(request).fetchall()
        connection.close()
        return result

    def request_nomination_by_entreprise_name(self, entreprise_name):
        connection = self.get_db_connection()
        request = "SELECT U.last_name, U.first_name, E.place, C.contact FROM Candidacy as C Join Users as U ON U.id = C.user_id JOIN Enterprise as E ON E.id = C.enterprise_id WHERE E.name = '" + entreprise_name +"'"
        result = connection.execute(request).fetchall()
        connection.close()
        return result
            
    def request_nomination_by_lastname(self, lastname):
        connection = self.get_db_connection()
        request = "SELECT Enterprise.name, Enterprise.place, Candidacy.contact FROM Candidacy, Enterprise WHERE (SELECT id from Users WHERE LOWER(last_name) = '"+ lastname.lower() +"') = Candidacy.user_id AND Candidacy.enterprise_id = Enterprise.id"
        result = connection.execute(request).fetchall()
        connection.close()
        return result
    
    def request_nomination_by_firstname(self, first_name):
        connection = self.get_db_connection()
        request = "SELECT Entreprise.name, Entreprise.place, Candidature.contact FROM Candidature, Entreprise WHERE (SELECT id from Users WHERE LOWER(first_name) = '"+ first_name.lower() +"') = Candidature.user_id AND Candidature.enterprise_id = Entreprise.id"
        result = connection.execute(request).fetchall()
        connection.close()
        return result

    def request_nomination_by_firstname_lastname(self, first_name, lastname):
        connection = self.get_db_connection()
        request = "SELECT Entreprise.name, Entreprise.place, Candidature.contact FROM Candidature, Entreprise WHERE (SELECT id from Users WHERE LOWER(last_name) = '"+ lastname.lower() + "' AND LOWER(first_name) = '"+ first_name.lower() +"') = Candidature.user_id AND Candidature.enterprise_id = Entreprise.id"
        result = connection.execute(request).fetchall()
        connection.close()
        return result
    
    def request_all_nomination(self):
        connection = self.get_db_connection()
        request = "SELECT Users.last_name, Users.first_name, Enterprise.name, Enterprise.place, Candidacy.contact, Candidacy.date FROM Users, Candidacy, Enterprise WHERE Users.id = Candidacy.user_id AND Candidacy.enterprise_id = Enterprise.id"
        result = connection.execute(request).fetchall()
        connection.close()
        return result