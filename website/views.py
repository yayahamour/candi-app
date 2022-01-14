from flask import Blueprint, render_template, flash, redirect, url_for, request
from form_add import LoginForm
import sqlite3

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('base.html', boolean = True)

# to check
# @views.route('/form_add.html', methods = ['GET', 'POST'])
# def form_add():
#     form_add = LoginForm()
#     if form_add.validate_on_submit():
#         entreprise = request.form["Entreprise"]
#         lieu = request.form["Lieu"]
#         contact = request.form["Contact"]
#         # date = request.form["Date"]
#         # date_de_relance = request.form["Date de relance"]
#         # statut = request.form["Statut"]

#         c = sqlite3.connect('website/DB/base_test.db')
#         nomination = c.cursor()
#         # check if entreprise is in Entreprise table
#         is_entreprise = nomination.execute("SELECT id, name FROM Entreprise WHERE name = ?", (entreprise,))
#         if not is_entreprise :
#             # add new enterprise in Entreprise table
#             nomination.execute("INSERT INTO Entreprise (name, lieu) VALUES (?,?)", (entreprise, lieu,))
#             new_enterprise_id = ("SELECT MAX(id) FROM Entreprise")
#             # add new nomination in Candidature table
#             nomination.execute("INSERT INTO Candidature (user_id, enterprise_id, contact) VALUES (?, ?, ?)", (user_id, new_enterprise_id, contact,))
#         else :
#             enterprise_id = is_entreprise[0]
#             nomination.execute("INSERT INTO Candidature (user_id, enterprise_id, contact)",(user_id, enterprise_id, contact,))
#         c.commit()

#         flash('Candidature ajoutée pour {}'.format(form_add.enterprise.data))

#         return redirect(url_for('board'))
#     return render_template('board.html', form_add=form_add)