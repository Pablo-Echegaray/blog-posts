from flask import Blueprint

bp = Blueprint('auth', __name__, url_prefix= '/auth')


@bp.route('/register')
def register():
    return 'Págin de register'

@bp.route('/login')
def login():
    return 'Página de login'

@bp.route('/profile')
def profile():
    return 'Página de profile'