from flask import Blueprint, render_template, abort, redirect, session, request, url_for, flash
from flask_login import current_user, login_required
from flask_mail import Message
from myproject import mail, db, detect, random_code
from myproject.employer.forms import RegistrationForm, UpdateForm, CreateJob
from myproject.media.handle_media import handle
from myproject.models import Users, Jobs

from myproject import check_cat

employer = Blueprint('employer', __name__, template_folder='temp', url_prefix='/employer')


@employer.route('/main')
@login_required
@check_cat
def main():
    i = Jobs.query.filter_by(user_id=current_user.id)  # .filter_by(applied_for_this_job>=1)
    return render_template('employer_main.html', jobs=i)


@employer.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(detect(current_user, 'main'))
    form = RegistrationForm()
    if form.validate_on_submit():
        print('sad')
        session['employer_email'] = form.email.data
        session['employer_username'] = form.username.data
        session['employer_password'] = form.password.data
        session['employer_gender'] = form.gender.data
        session['employer_phone_number'] = form.phone_number.data
        session['employer_address_street'] = form.street.data
        session['employer_address_city'] = form.city.data
        session['employer_address_province'] = form.province.data
        session['employer_address_country'] = form.country.data
        session['employer_code'] = random_code()
        message = Message('confirmation code', sender='jousefgamal46@gmail.com', recipients=[form.email.data])
        message.body = f'your confirmation code: {session["employer_code"]}'
        message.html = render_template('employer_confirmation.html')
        mail.send(message)
        session['employer_confirm'] = True
        flash('check your email to verify your account')
    print(form.errors)
    return render_template('employer_register.html', form=form)


@employer.route('/confirmation')
def confirmation():
    if current_user.is_authenticated:
        return abort(404)
    confirm = request.args.get('code')
    print(confirm)
    if session['employer_confirm']:
        if confirm == session['employer_code']:
            print('sad')
            user = Users(email=session['employer_email'], username=session['employer_username'],
                         password=session['employer_password'],
                         address_province=session['employer_address_province'],
                         phone_number=session['employer_phone_number'],
                         address_street=session['employer_address_street'],
                         address_city=session['employer_address_city'],
                         address_country=session['employer_address_country'], male=session['employer_gender'],
                         type_of_account=True)
            try:
                db.session.add(user)
                print('ddd')
                db.session.commit()
                return render_template('employer_successful_added.html')
            except:
                db.session.rollback()
                return abort(404)
        else:
            session['code'] = ''
            return redirect(url_for('employer.register'))
    else:
        return abort(404)


@employer.route('/update', methods=['post', 'get'])
@login_required
@check_cat
def update():
    form = UpdateForm()
    if form.validate_on_submit():
        print('sad')
        current_user.username = form.username.data
        current_user.phone_for_contact = form.phone_number.data
        current_user.address_street = form.street.data
        current_user.address_city = form.city.data
        current_user.address_province = form.province.data
        current_user.address_country = form.country.data
        if form.picture.data:
            current_user.profile_pic = handle(form.picture.data)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            return render_template('something_went_wrong.html')
    # ----------------------     filling the form with the current_user data
    form.username.data = current_user.username
    form.street.data = current_user.address_street
    form.city.data = current_user.address_city
    form.province.data = current_user.address_province
    form.country.data = current_user.address_country
    form.phone_number.data = current_user.phone_number
    print(form.errors)
    return render_template('employer_update.html', form=form)


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
    return render_template('employer_account.html')


@employer.route('/post_job', methods=['post', 'get'])
@login_required
@check_cat
def post_job():
    form = CreateJob()
    if form.validate_on_submit():
        new_job = Jobs(text=form.text.data, title=form.title.data, user_id=current_user.id,
                       address_province=form.province.data,
                       address_country=form.country.data, phone_number=form.phone_for_contact.data,
                       location=form.street.data + ' ' + form.city.data)
        try:
            print('sad')
            db.session.add(new_job)
            db.session.commit()
            flash('job created successfully')
            return render_template('employer_job_successfully_added.html')
        except Exception as e:
            db.session.rollback()
            return render_template('something_went_wrong.html', e=e)

    return render_template('employer_post_job.html', form=form)

# @employer.route('')
