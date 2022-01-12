from dataclasses import dataclass 

@dataclass
class Users : 
    name : str 
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
    
    def add_nomination():
        pass 
    