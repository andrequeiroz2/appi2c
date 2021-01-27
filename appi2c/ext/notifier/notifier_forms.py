from flask_wtf import FlaskForm
from wtforms import (StringField,
                     SubmitField,
                     IntegerField)
from appi2c.ext.notifier.notifier_models import Notifier
from wtforms.validators import InputRequired, Length, ValidationError
from flask_login import current_user
from wtforms.widgets import HiddenInput


class NotifierForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(min=5, max=120, message=('Max 120 digits'))])
    token = StringField('Token', validators=[InputRequired(), Length(max=120, message=('Max 120 digits'))])
    chat_id = StringField('Chat ID', validators=[InputRequired(), Length(max=120, message=('Max 120 digits'))])
    submit = SubmitField('Insert')

    def validate_name(self, name):
        notifier = Notifier.query.filter_by(name=name.data).filter_by(user_id=current_user.id).first()
        if notifier is not None:
            raise ValidationError('Please use a different notifier name.')


class EditNotifierForm(FlaskForm):
    id = IntegerField(widget=HiddenInput())
    name = StringField('Name', validators=[InputRequired(), Length(min=5, max=120, message=('Max 120 digits'))])
    token = StringField('Token', validators=[InputRequired(), Length(max=120, message=('Max 120 digits'))])
    chat_id = StringField('Chat ID', validators=[InputRequired(), Length(max=120, message=('Max 120 digits'))])
    submit = SubmitField('Confirm')

    def validate_name(self, name):
        notifier = Notifier.query.filter_by(name=name.data).filter_by(user_id=current_user.id).first()
        if notifier is not None:
            if self.id.data != notifier.id:
                raise ValidationError('Please use a different notifier name.')
