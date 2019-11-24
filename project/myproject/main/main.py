import datetime
import json

from flask import Blueprint, render_template, flash, session, Markup, request, redirect, abort, jsonify, url_for
from flask_login import current_user, login_user, login_required, logout_user
from flask_mail import Message
from werkzeug.security import generate_password_hash

from myproject import detect, random_code, mail, db
from myproject.main.forms import ResetForm, Login, FormRecover
from myproject.models import Users

main = Blueprint('main', __name__, template_folder='temp')


@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(detect(current_user, 'main'))
    form = Login()
    if form.validate_on_submit():
        u = Users.query.filter_by('email' == form.email.data).first()
        if u is None:
            flash(Markup("email doesn't exist try <a href='/' class='alert-link'>register</a> instead"))
        elif u.check_password(form.password.data):
            login_user(u, remember=True, duration=datetime.timedelta(weeks=52))

            next = request.args.get('next')

            if next is None or not next[0] == '/':
                next = detect(current_user, 'main')
            return redirect(next)
        else:
            flash("email doesn't exists or password is wrong")

    return render_template('login.html', form=form)


@main.route('/forget_password', methods=['GET', 'POST'])
def forgot_password():
    if current_user.is_authencitcated:
        return redirect(detect(current_user, 'main'))
    session['reset_true'] = True
    form = ResetForm()
    if form.validate_on_submit():
        u = Users.query.filter_by('email' == form.email.data).first()
        if u is None:
            flash(Markup("email doesn't exist try to <a href='/'>register</a>"))
        else:
            session['user'] = u.id
            message = Message('confirmation code', sender='jousefgamal46@gmail.com', recipients=[form.email.data])
            session['reset_code'] = random_code()
            message.body = f'your reset code: copy this link and put it in browser {url_for("employer.reset")}?' \
                           f'reset_code={session["reset_code"]}'  # ----- _external for url_for is external
            message.html = render_template('reset_email.html')
            mail.send(message)
            return redirect(detect(current_user, 'reset'))
    return render_template('forget_password.html')


@main.route('/reset')
def reset():
    if current_user.is_authenticated:
        return redirect(detect(current_user, 'update'))
    if not session['reset_true']:
        return abort(404)
    de = request.args.get('reset_code')
    try:
        if de == session['reset_code']:
            form = FormRecover()
            if form.validate_on_submit():
                d = Users.query.get(session['user'])
                d.password = generate_password_hash(form.password.data)
                db.session.commit()
                return redirect(detect(current_user, 'login'))
            else:
                return render_template('recover.html', form=form)
    except:
        return abort(404)
    return redirect('/')


@main.route('/change')
@login_required
def change():
    form = FormRecover()
    if form.validate_on_submit():
        current_user.password = generate_password_hash(form.password.data)
        db.session.commit()
        return render_template('successful_changed.html')
    return render_template('change.html')


@main.route('/get_province_for_country')
def get_province_for_country():
    t = request.args.get('country')
    if not t in ['Eg', 'Jo', 'Sa']:
        if current_user.is_authenticated:
            logout_user()
            return abort(404)
        else:
            return abort(404)
    content = open(f'/json/{t}.json')
    data = json.load(content)
    return jsonify(data)


@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


@main.route('/')
def main():
    if current_user.is_authenticated:
        return redirect(detect(current_user,'main'))
    return render_template('main.html')
