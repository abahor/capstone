from flask import Blueprint, render_template, abort, redirect, session, request, url_for, flash
from flask_babel import gettext, lazy_gettext
from flask_login import login_required, current_user
from flask_mail import Message

# from geopy.geocoders import Nominatim
from myproject import mail, db
from myproject import random_code
from myproject.employee.forms import UpdateForm, RegistrationForm
from myproject.models import Users, Jobs

from myproject import check_cat, detect
from myproject.media.handle_media import handle

from myproject.employer.view import check_gender

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


# <<<<<<< HEAD
# @employee.route('/nearby_jobs')
# @login_required
# @check_cat
# def nearby_jobs():
#     coords = request.args.get('coords')
#     lat = coords.split(' ')[0]
#     long = coords.split(' ')[1]
#     # geolocator = Nominatim(user-agent='my user_agent ') # 000000000000000000000000000
#     location = geolocator.reverse(lat,long)
#     jobs = Jobs.query.search(location.address)
#     return render_template('nearby_jobs.html',jobs=jobs)
# =======
# @employee.route('/nearby_jobs')
# @login_required
# @check_cat
# def nearby_jobs():
#     coords = request.args.get('coords')
#     lat = coords.split(' ')[0]
#     long = coords.split(' ')[1]
#     geolocator = Nominatim(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
#                                       'like Gecko) Chrome/75.0.3770.100 Safari/537.36')
#     location = geolocator.reverse(lat, long)
#     jobs = Jobs.query.search(location.address)
#     return render_template('nearby_jobs.html', jobs=jobs)


# >>>>>>> 7c31a97da4897940b87ce32f61f583dbbe4b7ee9


@employee.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(detect(current_user, 'main'))

    form = RegistrationForm()
    if form.validate_on_submit():
        session['employee_email'] = form.email.data
        session['employee_username'] = form.username.data
        session['employee_password'] = form.password.data
        session['employee_phone_number'] = form.phone_number.data
        session['employee_address_street'] = form.street.data
        session['employee_address_city'] = form.city.data
        session['employee_address_province'] = form.province.data
        session['employee_address_country'] = form.country.data
        session['employee_gender'] = form.gender.data
        session['employee_code'] = random_code()
        print(session['employee_code'])
        message = Message("confirmation code", sender='jouefgamal46@gmail.com',
                          recipients=[form.email.data])  # --------       change it to the domain account
        message.body = f'your confirmation code: {session["employee_code"]}'
        message.html = render_template('employee_confirmation.html')
        session['employee_confirm'] = True
        try:
            mail.send(message)
        except:
            return abort(404)
        flash(gettext('check your email to verify your account'))
    print(form.errors)
    return render_template('employee_register.html', form=form)


@employee.route('/confirmation')
def confirmation():
    if current_user.is_authenticated:
        return abort(404)
    confirm = request.args.get('employee_code')
    try:
        if session['employee_confirm']:
            print(session['employee_code'])
            if confirm == session['employee_code']:
                user = Users(email=session['employee_email'], username=session['employee_username'],
                         password=session['employee_password'],
                         address_street=session['employee_address_street'],
                         address_city=session['employee_address_city'],
                         address_province=session['employee_address_province'],
                         phone_number=session['employee_phone_number'],
                         address_country=session['employee_address_country'],
                         male=check_gender(session['employee_gender']),
                         type_of_account=False)
            try:
                db.session.add(user)
                db.session.commit()
                flash(lazy_gettext('account has been verified'))
            except:
                db.session.rollback()
                return abort(404)
            return render_template('employee_successful_added.html')
            # except Exception as e:
            #     db.session.rollback()
            #     return render_template('somethong_Went_wrong', e=e)
        else:
            print('sad')
            return abort(404)
    except:
        # return redirect(url_for('employee.register'))
        return abort(404)


@employee.route('/update', methods=['post', 'get'])
@login_required
@check_cat
def update():
    form = UpdateForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.phone_number = form.phone_number.data
        current_user.address_street = form.street.data
        current_user.address_city = form.city.data
        current_user.address_province = form.province.data
        current_user.address_country = form.country.data
        if form.picture.data:
            current_user.profile_pic = handle(form.picture.data)
        db.session.commit()
    # ----------------------     filling the form with the current_user data
    form.username.data = current_user.username
    form.street.data = current_user.address_street
    form.city.data = current_user.address_city
    form.phone_number.data = current_user.phone_number
    form.province.data = current_user.address_province
    form.country.data = current_user.address_country
    return render_template('employee_update.html', form=form)


@employee.route('/search')
@login_required
@check_cat
def search():
    search_text = request.args.get('q')
    if not search_text:
        abort(404)
    jobs = Jobs.query.search(search_text).all()
    return render_template('search.html', jobs=jobs)


@employee.route('/apply')
@login_required
@check_cat
def apply():
    jb = request.args.get('job_id')
    try:
        job = Jobs.query.get(int(jb))
    except:
        return abort(404)
    if not job:
        return abort(404)
    job.applied_for_this_job += 1
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return abort(404, e)
    return render_template('apply.html', job=job)


@employee.route('/account')
@login_required
@check_cat
def account():
    return render_template('employee_account.html')
