import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort


app = Flask(__name__)
# app.config['SECRET_KEY'] ='azerty'

def get_db_connection():
    conn = sqlite3.connect('base_test.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM User WHERE id = ?',(post_id,)).fetchall()
    conn.close()
    return post


@app.route('/Board')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT last_name, first_name, telephone_number, e_mail , password FROM User').fetchall()
    conn.close()
    return render_template('board.html', name_table = "Candidat",User=posts)


