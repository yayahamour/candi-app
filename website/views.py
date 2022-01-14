from flask import Blueprint, render_template, request, flash, redirect, url_for
from website.Request import Request as Req

views = Blueprint('views', __name__)

@views.route('/')
def home():
    render_template('base.html', boolean = True)
    return redirect(url_for('auth.login'))

@views.route('/board', methods=['GET'])
def board():
    req = Req()
    return render_template('board.html', title = ["Nom", "Ville","Contact",""],name_table = "Candidat",User=req.request_nomination_by_id(request.args.get("id")))

