import time

from myproject import app
from flask import render_template, request, redirect
from sqlalchemy import exc


# from myproject.models import Users, Jobs
# from flask_admin.contrib.sqla import ModelView
# admin.add_view(ModelView(Users, db.session))
# admin.add_view(ModelView(Jobs, db.session))

@app.errorhandler(404)
def handler(e):
    return render_template('not_found.html'), 404


@app.errorhandler(exc.DisconnectionError)
def h_request(e):
    time.sleep(5)
    try:
        return redirect(request.url_rule)
    except:
        return render_template('somethong_Went_wrong.html'), 404


@app.errorhandler(exc.DatabaseError)
def h_bad_request(e):
    time.sleep(5)
    try:
        return redirect(request.url_rule)
    except:
        return render_template('somethong_Went_wrong.html'), 404



@app.errorhandler(exc.DBAPIError)
def _bad_request(e):
    time.sleep(5)
    try:
        return redirect(request.url_rule)
    except:
        return render_template('somethong_Went_wrong.html'), 404


@app.errorhandler(exc.InternalError)
def _request(e):
    time.sleep(5)
    try:
        return redirect(request.url_rule)
    except:
        return render_template('somethong_Went_wrong.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
