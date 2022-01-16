from os import name
import sqlite3
from . import db 
from .models import Entreprise, Candidature, User
from sqlalchemy.sql import select 
from flask_login import current_user


class Request():
    
    def table_candidature_admin():
        # Récupère toute les requetes (Entreprise name/place pas bon)
        conn = db.engine.connect()
        target = select(User.first_name, User.last_name, Entreprise.name, Entreprise.place, Candidature.contact, Candidature.date, Candidature.status).join(User).where(User.id == Candidature.user_id ).join(Entreprise).where(Entreprise.id == Candidature.enterprise_id).order_by(Candidature.date)
        result = conn.execute(target)
        return result

    def table_candidature_user():
        # Fonctionne pour n'avoir que les requette du current User (Entreprise name/place pas bon)
        conn = db.engine.connect()
        target = select(User.first_name, User.last_name, Entreprise.name, Entreprise.place, Candidature.contact, Candidature.date, Candidature.status).where(User.id == Candidature.user_id , Candidature.enterprise_id == Entreprise.id, current_user.email == User.email).order_by(Candidature.date)
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