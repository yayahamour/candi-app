from flask import Blueprint, render_template, request, flash, redirect, url_for
from website.Request import Request as Req
from website.form_add import LoginForm

views = Blueprint('views', __name__)

@views.route('/')
def home():
    render_template('base.html', boolean = True)
    return redirect(url_for('auth.login'))

@views.route('/board', methods=['GET'])
def board():
    req = Req()
    is_admin = request.args.get("admin")
    if (is_admin == "True"):
        return render_template('board.html', title = ["Nom", "Prenom","Nom Entreprise", "Ville","Contact",""],name_table = "Candidat",User=req.request_all_nomination())
    elif (is_admin == "False"):
        return render_template('board.html', title = ["Nom Entreprise", "Ville","Contact",""],name_table = "Candidat",User=req.request_nomination_by_id(request.args.get("id")))

@views.route('/formulaire', methods=['GET', 'POST'])
def formulaire():
    return render_template('form_add.html', form_add=LoginForm())