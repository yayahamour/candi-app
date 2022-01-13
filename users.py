from dataclasses import dataclass 
import sqlite3

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
        conn = sqlite3.connect('base_test.db')
        my_cursor = conn.cursor()
        my_cursor.execute("""SELECT * FROM User""")
        rows = my_cursor.fetchall()
        for row in rows:
            print(row)

rudy = Apprenant("BOUREZ","Rudy","mail@mail.com","*****","DEV IA","0606060606")

rudy.modify_nomination()