from dataclasses import dataclass
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user
from website.users import Apprenant, Admin
import os
import sqlite3

connection = sqlite3.connect('website/DB/base_test.db', check_same_thread=False)
cur = connection.cursor()

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        cur.execute("SELECT * FROM User WHERE e_mail = ?",
                    (email,)
                    )
        row = cur.fetchone()
        if row:
            if row[6] == 0:
                user = Apprenant(row[0],row[1],row[2],row[4],row[5],row[3])
            elif row[6] == 1:
                user = Admin(row[0],row[1],row[2],row[4],row[5])
            if user:
                if user.password == password:
                    flash('Logged in successfully!', category='success')
                    
                    login_user(user, remember= True)
                    os.environ["Id"] = str(user.id)
                    return redirect(url_for('views.board', id = user.id, admin = user.is_admin))
                else:
                    flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
            
    return render_template('login.html', boolean = True)

@auth.route('/logout')
def logout():
    logout_user
    return redirect(url_for('auth.login'))