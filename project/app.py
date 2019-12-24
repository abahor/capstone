from myproject import app
# from myproject.models import Users, Jobs
# from flask_admin.contrib.sqla import ModelView
# admin.add_view(ModelView(Users, db.session))
# admin.add_view(ModelView(Jobs, db.session))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
