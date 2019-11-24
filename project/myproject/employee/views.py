from flask import Blueprint, render_template, abort, redirect, session, request, url_for
from flask_login import login_required, current_user
from flask_mail import Message

from myproject import mail, db
from myproject import random_code
from myproject.employee.forms import UpdateForm, RegistrationForm
from myproject.models import Users

from project.myproject import check_cat, detect
from project.myproject.media.handle_media import handle

employee = Blueprint('employee', __name__, template_folder='temp', url_prefix='/employee')


# @employee.route('/login', methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:
#         redirect(url_for('employee.main'))
#     form = LoginForm()
#     if form.validate_on_submit():
#         u = Users.query.filter_by('email' = form.email.data).first()
#         if u.check_password(form.password.data):
#             login_user(u, remember=True, duration=datetime.timedelta(weeks=52))
#
#             next = request.args.get('next')
#
#             if next is None or not next[0] == '/':
#                 next = detect(current_user)
#             return redirect(next)
#
#     return render_template('login.html', form=form)


@employee.route('/main')
@login_required
@check_cat
def main():
    return render_template('employee_main.html')

@employee.route('/nearby_jobs')
@login_required
@check_cat
def nearby_jobs():

    return render_template('nearby_jobs.html')

@employee.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        if current_user.employer:
            return redirect(detect(current_user,'main'))

    form = RegistrationForm()
    if form.validate_on_submit():
        session['email'] = form.email.data
        session['username'] = form.username.data
        session['password'] = form.password.data
        session['address_street'] = form.street.data
        session['address_city'] = form.city.data
        session['address_province'] = form.province.data
        session['address_country'] = form.country.data
        session['gender'] = form.gender.data
        session['code'] = random_code()
        message = Message("confirmation code", sender='jouefgamal46@gmail.com',
                          recipients=[form.email.data])  # --------       change it to the domain account
        message.body = f'your confirmation code: {session["code"]} '
        message.html = render_template('confirmation_code.html')
        mail.send(message)
        session['confirm'] = True
    return render_template('register.html', form=form)


@employee.route('/confirmation')
def confirmation():
    if current_user.is_authenticated:
        return abort(404)
    confirm = request.args.get('code')
    if session['confirm']:
        if confirm == session['code']:
            user = Users(email=session['email'], username=session['username'], password=session['password'],
                         address_street=session['address_street'], address_city=session['address_city'],
                         address_province=session['address_province'],
                         address_country=session['address_country'], male=session['gender'], type_of_account=False)
            try:
                db.session.add(user)
                db.session.commit()
                return render_template('successful_added.html')
            except:
                db.session.rollback()
    else:
        return redirect(url_for('employee.register'))


@employee.route('/update')
@login_required
@check_cat
def update():
    form = UpdateForm()
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

# @employee.route('/change')
# @login_required
# def change():
#     form = formRecover()
#     if form.validate_on_submit():
#         current_user.password = generate_password_hash(form.password.data)
#         db.session.commit()
#         return render_template('successful_changed.html')
#     return render_template('change.html')
