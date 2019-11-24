from flask import Blueprint, render_template, abort, redirect, session, request
from flask_login import current_user, login_required
from flask_mail import Message
from myproject import mail, db, detect, random_code
from myproject.employer.forms import RegistrationForm, UpdateForm, CreateJob
from myproject.media.handle_media import handle
from myproject.models import Users

from project.myproject import check_cat

employer = Blueprint('employer', __name__, template_folder='temp', url_prefix='/employer')


@employer.route('/main')
@login_required
@check_cat
def main():

    return render_template('employer_main.html')

@employer.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(detect(current_user, 'main'))
    form = RegistrationForm()
    if form.validate_on_submit():
        session['email'] = form.email.data
        session['username'] = form.username.data
        session['password'] = form.password.data
        session['gender'] = form.gender.data
        session['address_street'] = form.street.data
        session['address_city'] = form.city.data
        session['address_province'] = form.province.data
        session['address_country'] = form.country.data
        session['code'] = random_code()
        message = Message('confirmation code', sender='jousefgamal46@gmail.com', recipients=[form.email.data])
        message.body = f'your confirmation code: {session["code"]}'
        message.html = render_template('confirmation.html')
        mail.send(message)
        session['confirm'] = True
    return render_template('register.html')


@employer.route('/confirmation')
def confirmation():
    if current_user.is_authenticated:
        return abort(404)
    confirm = request.args.get('code')
    if session['confirm']:
        if confirm == session['code']:
            user = Users(email=session['email'], username=session['username'], password=session['password'],
                         address_province=session['address_province'],
                         address_street=session['address_street'], address_city=session['address_city'],
                         address_country=session['address_country'], male=session['gender'], type_of_account=True)
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


# @employer.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect('/')
@employer.route('/account')
@login_required
@check_cat
def account():
    # show the account
    return render_template('account.html')

@employer.route('/post_job')
@login_required
@check_cat
def post_job():
    form = CreateJob()
    if form.validate_on_submit():
        
    return render_template('post_job.html',form=form)
