from os import name
from . import db 
from .models import Entreprise, Candidature, User
from sqlalchemy.sql import select , delete, update 
from flask_login import current_user


class Request():
    
    # Dashboard Admin 
    def table_candidature_admin():
        conn = db.engine.connect()
        target = select(User.first_name, User.last_name, Entreprise.name, Entreprise.place, Candidature.contact, Candidature.date, Candidature.status).join(User).where(User.id == Candidature.user_id ).join(Entreprise).where(Entreprise.id == Candidature.enterprise_id).order_by(Candidature.date)
        result = conn.execute(target)
        return result

    # Dashbord Users
    def table_candidature_user():
        conn = db.engine.connect()
        target = select(User.first_name, User.last_name, Entreprise.name, Entreprise.place, Candidature.contact, Candidature.date, Candidature.status).where(User.id == Candidature.user_id , Candidature.enterprise_id == Entreprise.id, current_user.email == User.email).order_by(Candidature.date)
        result = conn.execute(target)
        return result   
    
    def update_status_accepte(one):
        pass
        # target = Candidature.query.filter_by(user_id = one.id).first().update(status ="Accepté")
        # conn = db.engine.connect()
        # target = update(Candidature).where( user_id = one.id).values(status = 'Accepté')
        # result = conn.execute(target)

    
    # Delete element 
    def delete_nomination(one):
        pass
        # conn = db.engine.connect()
        # target = delete(Candidature).where( Candidature.user_id == one.id )
        # result = conn.execute( target)
        
        
        
    
    
    
# ----------------------------------------------------------------> Note
# db.session.query(Entreprise).all()
# Revient au meme que Entreprise.query.all() -- 
# A revoir pour la différence de passé par la db.session ? 
        

# # Pour voir dans les tables : 
#     target = User.query.all()
#     for use in target :
#         print('Entreprise  : ' , use.name)
        
    # target = db.session.query(Candidature).all()
    # for i in target :
    #     print(i.id)