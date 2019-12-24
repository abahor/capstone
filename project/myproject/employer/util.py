from flask_babel import lazy_gettext
from wtforms import ValidationError


class Unique(object):
    def __init__(self, model, field, message=lazy_gettext(u'This element already exists.')):
        self.model = model
        self.field = field
        self.message = message

    def __call__(self, form, field):
        check = self.model.query.filter(self.field == field.data).first()
        if check:
            raise ValidationError(self.message)
