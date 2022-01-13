from dataclasses import dataclass
from flask import Blueprint, render_template, request, flash, redirect, url_for
# from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
import sqlite3

connection = sqlite3.connect('base_test.db', check_same_thread=False)
cur = connection.cursor()

auth = Blueprint('auth', __name__)

@dataclass
class User:
    id: int
    last_name: str
    first_name: int
    telephone: str
    e_mail: str
    password: int
    is_admin: bool
    is_active: bool
    
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
            user = User(row[0], row[1], row[2], row[3], row[4], row[5], row[6], is_active=False)
            if user:
                if user.password == password:
                    flash('Logged in successfully!', category='success')
                    
                    login_user(user, remember= True)
                    return redirect(url_for('views.home'))
                else:
                    flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
            
    return render_template('login.html', boolean = True)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))