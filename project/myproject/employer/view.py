import datetime

from flask import Blueprint, render_template, abort, redirect, flash, session, request, url_for
from flask_login import current_user, login_required, logout_user, login_user
from flask_mail import Message
from markupsafe import Markup
from myproject import mail, db, detect, randomcode
from myproject.employer.forms import RegisterationForm, LoginForm, updateForm, formRecover, resetForm
from myproject.models import Users
from werkzeug.security import generate_password_hash
from myproject.employer.media.handle_name import handle

employer = Blueprint('employer', __name__, template_folder='temp', url_prefix='/employer')


# @employer.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         u = Users.query.filter_by('email' = form.email.data).first()
#         if u is None:
#             flash("email doens't exist or password is wrong")
#         else:
#             if u.check_password(form.password.data):
#                 login_user(u, remember=True, duration=datetime.timedelta(weeks=52))
#                 return redirect(detect(current_user,'main'))
#             else:
#                 flash("email doens't exist or password is wrong")
#
#     return render_template('login.html', form=form)


@employer.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(detect(current_user,'main'))
    form = RegisterationForm()
    if form.validate_on_submit():
        session['email'] = form.email.data
        session['username'] = form.username.data
        session['password'] = form.password.data
        session['address_street'] = form.address_street.data
        session['address_city'] = form.address_city.data
        session['address_province'] = form.address_province.data
        session['code'] = randomcode()
        message = Message('confirmation code', sender='jousefgamal46@gmail.com', recipients=[form.email.data])
        message.body = f'your confirmaion code: {session["code"]}'
        message.html = render_template('confirmation.html')
        mail.send(message)
        session['confirm'] = True
    return render_template('register.html')


@employer.route('/confirmaion')
def confirmaion():
    if current_user.is_authenticated:
        return abort(404)
    confirm = request.args.get('code')
    if session['confirm']:
        if confirm == session['code']:
            user = Users(email=session['email'], username=session['username'], password=session['password'],
                         address_street=session['address_street'], address_city=session['address_city'],
                         address_country=session['address_country'], type=True)
            try:
                db.session.add(user)
                db.session.commit()
                return render_template('successful_added.html')
            except:
                db.session.rollback()
    else:
        return abort(404)




@employer.route('/update')
@login_required
def update():
    form = updateForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.address_street = form.street.data
        current_user.address_city = form.city.data
        current_user.address_province = form.province.data
        current_user.address_country = form.country.data
        current_user.profile_pic = handle(form.picture)
    # ----------------------     filling the form with the current_user data
    form.username.data = current_user.username
    form.street.data = current_user.address_street
    form.city.data = current_user.address_city
    form.province.data = current_user.address_province
    form.country.data = current_user.address_country
    return render_template('update.html', form=form)


# @employer.route('/change')
# @login_required
# def change():
#     form = formRecover()
#     if form.validate_on_submit():
#         current_user.password = generate_password_hash(form.password.data)
#         try:
#             db.session.commit()
#         except Exception as e:
#             return abort(404)
#         return render_template('successful_changed.html')
#     return render_template('change.html')


@employer.route('/forget_password', methods=['GET', 'POST'])
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
            message.body = f'your reset code: copy this link and put it in browser {url_for("employer.reset")}?resetcode={session["reset_code"]}' # ----- _external for url_for is extenral
            message.html = render_template('reset_email.html')
            mail.send(message)
            return redirect(url_for('employer.reset'))
    return render_template('forget_password.html')


@employer.route('/reset')
def reset():
    if current_user.is_authenticated:
        return redirect(detect(current_user,'update'))
    if session['reset_true'] != True:
        return abort(404)
    de = request.args.get('resetcode')
    try:
        if de == session['reset_code']:
            form = formRecover()
            if form.validate_on_submit():
                d = Users.query.get(session['user'])
                d.password = generate_password_hash(form.password.data)
                db.session.commit()
                return redirect(url_for('employer.login'))
            else:
                return render_template('recover.html', form=form)
    except Exception as e:
        abort(404)
    return redirect('/')


@employer.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')
