import datetime
import json

from flask import Blueprint, render_template, flash, session, Markup, request, redirect, abort, jsonify, url_for, \
    current_app
from flask_babel import gettext, gettext, lazy_gettext
from flask_login import current_user, login_user, login_required, logout_user
from flask_mail import Message
from werkzeug.security import generate_password_hash

from myproject import detect, random_code, mail, db
from myproject.main.forms import ResetForm, Login, FormRecover
from myproject.models import Users, Jobs

from myproject import check_cat

mained = Blueprint('mained', __name__, template_folder='temp')


@mained.route('/login', methods=['GET', 'POST'])
def login():
    print(gettext('Email'))
    print(request.accept_languages.best_match(['en', 'ar']))
    if current_user.is_authenticated:
        return redirect(detect(current_user, 'main'))
    form = Login()

    if form.validate_on_submit():
        u = Users.query.filter_by(email=form.email.data).first()
        if u is None:
            flash(Markup(gettext("email doesn't exist try") + " <a href='/' class='alert-link'>" + gettext("register")
                         + "</a> " + gettext("instead")))
        elif u.check_password(form.password.data):
            login_user(u, remember=True, duration=datetime.timedelta(weeks=52))

            forward = request.args.get('next')

            if forward is None or not forward[0] == '/':
                forward = detect(current_user, 'main')
            return redirect(forward)
        else:
            flash(gettext("email doesn't exists or password is wrong"))
    print('sad ')
    print(form.errors)
    return render_template('log.html', form=form)
    # return render_template('login.html', form=form)
    # return 'sad'


@mained.route('/forget_password', methods=['GET', 'POST'])
def forgot_password():
    try:
        if current_user.is_authencitcated:
            return redirect(detect(current_user, 'main'))
    except:
        pass
    form = ResetForm()
    if form.validate_on_submit():
        print('good')
        u = Users.query.filter_by(email=form.email.data).first()
        if u is None:
            flash(Markup(gettext("email doesn't exist try to") + "<a href='/'>" + gettext("register") + "</a>"))
        else:
            session['user'] = u.id
            message = Message('confirmation code', sender='jousefgamal46@gmail.com', recipients=[form.email.data])
            session['reset_code'] = random_code()
            message.body = f'your reset code: copy this link and put it in browser {url_for("mained.reset")}?' \
                f'reset_code={session["reset_code"]}'  # ----- _external for url_for is external
            message.html = render_template('reset_email.html')
            mail.send(message)
            session['reset_true'] = True
            return redirect(detect(current_user, 'reset'))
    print(form.errors)
    return render_template('forget_password.html', form=form)


@mained.route('/reset', methods=['post', 'get'])
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


@mained.route('/change', methods=['post', 'get'])
@login_required
def change():
    form = FormRecover()
    if form.validate_on_submit():
        current_user.password = generate_password_hash(form.password.data)
        db.session.commit()
        flash(gettext('successfully changed your password'))
        return render_template('successful_changed.html')
    return render_template('change.html', form=form)


def country_translator(d):
    u = []
    for i in d:
        i['translate'] = lazy_gettext(i['translate'])
        u.append(i)
    return u

@mained.route('/get_province_for_country')
def get_province_for_country():
    t = request.args.get('country')
    if t not in ['Eg', 'Jo', 'Sa']:
        if current_user.is_authenticated:
            logout_user()
            return abort(404)
        else:
            return abort(404)
    # content = open(current_app.root_path + f'/json/{t}.json')
    # data = json.load(content)

    egypt = [
        {'state': "Alexandria Governorate", 'translate': "Alexandria Governorate"},
        {'state': "Aswan Governorate", 'translate': "Aswan Governorate"},
        {'state': "Asyut Governorate", 'translate': "Asyut Governorate"},
        {'state': "Beheira Governorate", 'translate': "Beheira Governorate"},
        {'state': "Beni Suef Governorate", 'translate': "Beni Suef Governorate"},
        {'state': "Cairo Governorate", 'translate': "Cairo Governorate"},
        {'state': "Dakahlia Governorate", 'translate': "Dakahlia Governorate"},
        {'state': "Damietta Governorate", 'translate': "Damietta Governorate"},
        {'state': "Faiyum Governorate", 'translate': "Faiyum Governorate"},
        {'state': "Gharbia Governorate", 'translate': "Gharbia Governorate"},
        {'state': "Giza Governorate", 'translate': "Giza Governorate"},
        {'state': "Ismailia Governorate", 'translate': "Ismailia Governorate"},

        {'state': "Kafr el-Sheikh Governorate", 'translate': "Kafr el-Sheikh Governorate"},
        {'state': "Luxor Governorate", 'translate': "Luxor Governorate"},
        {'state': "Matrouh Governorate", 'translate': "Matrouh Governorate"},
        {'state': "Minya Governorate", 'translate': "Minya Governorate"},
        {'state': "Monufia Governorate", 'translate': "Monufia Governorate"},

        {'state': "New Valley Governorate", 'translate': "New Valley Governorate"},
        {'state': "North Sinai Governorate", 'translate': "North Sinai Governorate"},
        {'state': "Port Said Governorate", 'translate': "Monufia Governorate"},
        {'state': "Qalyubia Governorate", 'translate': "Qalyubia Governorate"},
        {'state': "Qena Governorate", 'translate': "Qena Governorate"},
        {'state': "Red Sea Governorate", 'translate': "Red Sea Governorate"},
        {'state': "Sohag Governorate", 'translate': "Sohag Governorate"},

        {'state': "South Sinai Governorate", 'translate': "South Sinai Governorate"},
        {'state': "Suez Governorate", 'translate': "Suez Governorate"}
    ]
    jordan = [
        {'state': "Ajlun", 'translate': "Ajlun"},
        {'state': "Al 'Aqabah", 'translate': "Al 'Aqabah"},
        {'state': "Al Balqa'", 'translate': "Al Balqa'"},
        {'state': "Al Karak", 'translate': "Al Karak"},
        {'state': "Al Mafraq", 'translate': "Al Mafraq"},
        {'state': "'Amman", 'translate': "'Amman"},
        {'state': "At Tafilah", 'translate': "At Tafilah"},
        {'state': "Az Zarqa'", 'translate': "Az Zarqa'"},
        {'state': "Irbid", 'translate': "Irbid"},
        {'state': "Jarash", 'translate': "Jarash"},
        {'state': "Ma'an", 'translate': "Ma'an"},
        {'state': "Madaba", 'translate': "Madaba"}
    ]
    saudi = [
        {'state': "Al Bahah", 'translate': "Al Bahah"},
        {'state': "Al Hudud ash Shamaliyah", 'translate': "Al Hudud ash Shamaliyah"},
        {'state': "Al Jawf", 'translate': "Al Jawf"},
        {'state': "Al Madinah", 'translate': "Al Madinah"},
        {'state': "Al Qasim", 'translate': "Al Qasim"},
        {'state': "Ar Riyad", 'translate': "Ar Riyad"},
        {'state': "Ash Sharqiyah", 'translate': "Ash Sharqiyah"},
        {'state': "'Asir", 'translate': "'Asir"},
        {'state': "Ha'il", 'translate': "Ha'il"},
        {'state': "Jizan", 'translate': "Jizan"},
        {'state': "Makkah", 'translate': "Makkah"},
        {'state': "Najran", 'translate': "Najran"},
        {'state': "Tabuk", 'translate': "Tabuk"}
    ]
    # print(data)
    if t == 'Eg':
        data = country_translator(egypt)
    elif t == 'Jo':
        data = country_translator(jordan)
    elif t == 'Sa':
        data = country_translator(saudi)
    else:
        return abort(404)
    return jsonify(data)


@mained.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


@mained.route('/')
def main():
    if current_user.is_authenticated:
        return redirect(detect(current_user, 'main'))
    return render_template('main.html')


@mained.route('/about')
def about():
    return render_template('about.html')


@mained.route('/keep_job', methods=['post'])
@login_required
def keep_job():
    id_of_the_job = request.args.get('job_id')
    print(id_of_the_job)
    if not id_of_the_job:
        return abort(404)
    job = Jobs.query.get(id_of_the_job)
    if not job:
        abort(404)
    try:
        job.applied_for_this_job = 0
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return abort(404, e)
    return ''


@mained.route('/delete_this_job', methods=['post'])
@login_required
def delete_this_job():
    id_of_job = request.args.get('job_id')
    if not id_of_job:
        abort(404)
    job = Jobs.query.get(id_of_job)
    if not job:
        return abort(404)
    if job.user_id == current_user.id:
        db.session.delete(job)
        db.session.commit()
    else:
        # db.session.rollback()
        return abort(404)
    return 'deleted'


@mained.route('/show_details')
@login_required
def show_details():
    job_id = request.args.get('job_id')
    job = Jobs.query.get(job_id)
    if not job:
        return abort(404)
    job.applied_for_this_job += 1
    db.session.commit()
    return render_template('show_details.html', job=job)


@mained.route('/get_job')
@login_required
def get_job():
    city = request.args.get('city')
    print(city)
    # print(gettext(city, locale='en'))
    jobs = Jobs.query.filter_by(address_province=city).all()
    o = []
    if not jobs:
        return abort(404)
    for i in jobs:
        ob = {'title': i.title, 'text': i.text, 'link': '/show_details?job_id=' + str(i.id)}
        o.append(ob)
    return jsonify(o)
