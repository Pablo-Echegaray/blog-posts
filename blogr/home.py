from flask import Blueprint

bp = Blueprint('home', __name__)

@bp.route('/')
def index():
    return 'Página de Inicio'

@bp.route('/blog')
def blog():
    return 'Págin de blog'

