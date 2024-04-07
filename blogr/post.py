from flask import Blueprint, request, flash, redirect, url_for, g, render_template
from .auth import login_required
from .models import Post
from blogr import db

bp = Blueprint('post', __name__, url_prefix= '/post')


@bp.route('/posts')
@login_required
def posts():
    posts = Post.query.all()
    return render_template('admin/posts.html', posts = posts)

@bp.route('/create')
def create():
    return 'Página de create'

@bp.route('/update')
def update():
    return 'Página de update'