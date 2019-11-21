import datetime

from flask import Blueprint, render_template, abort, redirect, session, request, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from flask_mail import Message
from markupsafe import Markup
from myproject import mail, db, detect
from myproject.employee.forms import RegisterationForm, LoginForm, updateForm, formRecover, resetForm
from myproject.models import Users
from werkzeug.security import generate_password_hash

from project.myproject import randomcode

employee = Blueprint('employee', __name__, template_folder='temp', url_prefix='/employee')


@employee.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        redirect(url_for('employee.main'))
    form = LoginForm()
    if form.validate_on_submit():
        u = Users.query.filter_by('email' = form.email.data).first()
        if u.check_password(form.password.data):
            login_user(u, remember=True, duration=datetime.timedelta(weeks=52))

            next = request.args.get('next')

            if next is None or not next[0] == '/':
                next = detect(current_user)
            return redirect(next)

    return render_template('login.html', form=form)


@employee.route('/main')
@login_required
def main():
    return render_template('employee_main.html')


@employee.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        if current_user.employer:
            return redirect(url_for('employer.main'))
        else:
            return redirect(url_for('employee.main'))

    form = RegisterationForm()
    if form.validate_on_submit():
        session['email'] = form.email.data
        session['username'] = form.username.data
        session['password'] = form.password.data
        session['address_street'] = form.address_street.data
        session['address_city'] = form.address_city.data
        session['address_province'] = form.address_province.data
        session['code'] = randomcode()
        message = Message("confirmation code", sender='jouefgamal46@gmail.com',
                          recipients=[form.email.data])  # --------       change it to the domain account
        message.body = f'your confirmation code: {session["code"]} '
        message.html = render_template('confirmation_code.html')
        mail.send(message)
        session['confirm'] = True
    return render_template('register.html', form=form)


@employee.route('/confirmaion')
def confirmaion():
    if current_user.is_authenticated:
        return abort(404)
    confirm = request.args.get('code')
    if session['confirm']:
        if confirm == session['code']:
            user = Users(email=session['email'], username=session['username'], password=session['password'],
                         address_street=session['address_street'], address_city=session['address_city'],
                         address_country=session['address_country'], type=False)
            try:
                db.session.add(user)
                db.session.commit()
            except:
                db.session.rollback()

    return render_template('successful_added.html')


@employee.route('/update')
@login_required
def update():
    form = updateForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.city = form.city.data
        current_user.country = form.country.data
        current_user.province = form.province.data
    return render_template('update.html', form=form)


@employee.route('/change')
@login_required
def change():
    form = formRecover()
    if form.validate_on_submit():
        current_user.password = generate_password_hash(form.password.data)
        db.session.commit()
        return render_template('successful_changed.html')
    return render_template('change.html')


@employee.route('/forget_password', methods=['GET', 'POST'])
@login_required
def forgot_password():
    session['reset_true'] = True
    form = resetForm()
    if form.validate_on_submit():
        u = Users.query.filter_by('email' = form.email.data).first()
        if u is None:
            flash(Markup("email doesn't exist try to <a href='/'>register</a>"))
        else:
            session['user'] = u.id
            message = Message('confirmaion code', sender='jousefgamal46@gmail.com', recipients=[form.email.data])
            session['reset_code'] = randomcode()
            message.body = f'your reset code: {session["reset_code"]}'
            message.html = render_template('reset_email.html')
            mail.send(message)
            return redirect(url_for('employee.reset'))
    return render_template('forget_password.html')


@employee.route('/reset')
@login_required
def reset():
    de = request.args.get('resetcode')
    try:
        if de == session['reset_code']:
            form = formRecover()
            if form.validate_on_submit():
                d = Users.query.get(session['user'])
                d.password = generate_password_hash(form.password.data)
                db.session.commit()
                return redirect(url_for('employee.login'))
            else:
                return render_template('recover.html', form=form)
    except Exception as e:
        abort(404)
    return redirect('/')


@employee.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')
