import re
import sqlite3
from flask import Flask, render_template
from website import create_app
from website.Request import Request


app = Flask(__name__)
# app.config['SECRET_KEY'] ='azerty'

app = create_app()

if __name__ == '__name_':
    app.run(debug = True)
