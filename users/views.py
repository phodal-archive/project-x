from flask import Blueprint, render_template
from werkzeug.utils import redirect
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


users_mod = Blueprint('users', __name__, template_folder='templates', url_prefix='', static_folder='static')


class MyForm(Form):
    name = StringField('name', validators=[DataRequired()])


@users_mod.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/submit')
    return render_template('submit.html', form=form)