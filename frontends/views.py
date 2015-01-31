from flask import Blueprint, render_template

mod = Blueprint('frontends', __name__, template_folder='templates', url_prefix='')

@mod.route('/')
def home():
    return render_template('home.html')