from myproject import app
from flask import render_template
from sqlalchemy import exc

# from myproject.models import Users, Jobs
# from flask_admin.contrib.sqla import ModelView
# admin.add_view(ModelView(Users, db.session))
# admin.add_view(ModelView(Jobs, db.session))

@app.errorhandler(404)
def handler(e):
    return render_template('something_went_wrong.html'), 404

@app.errorhandler(exc.DisconnectionError)
def handle_bad_request(e):
    return render_template('somethong_Went_wrong'), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
