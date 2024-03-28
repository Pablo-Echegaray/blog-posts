from flask import Blueprint, render_template, request, url_for, redirect, flash, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from blogr import db

bp = Blueprint('auth', __name__, url_prefix= '/auth')


@bp.route('/register', methods = ('GET', 'POST'))
def register():
    
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User(username, email, generate_password_hash(password))
        
        #Validación de datos
        error = None
        # Comparando nombre de usuario con los existentes
        user_email = User.query.filter_by(email = email).first()
        if user_email == None:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        
    return render_template('auth/register.html')


@bp.route('/login')
def login():
    return render_template('auth/login.html')

@bp.route('/profile')
def profile():
    return 'Página de profile'