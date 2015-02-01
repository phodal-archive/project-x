from flask import Blueprint, render_template, request
from flask_mongoengine.wtf.orm import model_form
from werkzeug.utils import redirect

from users.forms import RegisterForm
from users.models import User


users_mod = Blueprint('users', __name__, template_folder='templates', url_prefix='', static_folder='static')

PostForm = model_form(User)

@users_mod.route('/register/account', methods=('GET', 'POST'))
def add_post():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        return redirect('/register/success')
    return render_template('register.html', form=form)