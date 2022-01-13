import re
import sqlite3
from flask import Flask, render_template
from website import create_app
from Request import Request


app = Flask(__name__)
# app.config['SECRET_KEY'] ='azerty'

@app.route('/')
def index():
    request = Request()
    return render_template('board.html', title = ["Nom", "Ville","Contact"],name_table = "Candidat",User=request.request_nomination_by_id(1))

app = create_app()

if __name__ == '__name_':
    app.run(debug = True)
