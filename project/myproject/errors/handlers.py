from flask import render_template
from myproject import app


@app.errorhandler(404)
def handler(e):
    return render_template('something_went_wrong.html')

