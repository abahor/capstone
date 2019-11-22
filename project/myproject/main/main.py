from flask import Blueprint,render_template


main = Blueprint('main',__name__,template_folder='temp')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        redirect(url_for('employee.main'))
    form = LoginForm()
    if form.validate_on_submit():
        u = Users.query.filter_by('email' = form.email.data).first()
        if u is None:
            flash(Markup("email doens't exist try <a href='/'>register</a> instead"))
        elif u.check_password(form.password.data):
            login_user(u, remember=True, duration=datetime.timedelta(weeks=52))

            next = request.args.get('next')

            if next is None or not next[0] == '/':
                next = detect(current_user,'main')
            return redirect(next)
        else:
            flash("email doesn't exists or password is wrong")

    return render_template('login.html', form=form)


@main.route('/forget_password', methods=['GET', 'POST'])
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

@main.route('/reset')
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

@main.route('/get_province_for_country')
def get_province_for_country():
    t = request.args.get('country')
    return jsonify()


@main.route('/change')
@login_required
def change():
    form = formRecover()
    if form.validate_on_submit():
        current_user.password = generate_password_hash(form.password.data)
        db.session.commit()
        return render_template('successful_changed.html')
    return render_template('change.html')
