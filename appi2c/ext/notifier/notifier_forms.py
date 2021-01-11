from flask_wtf import FlaskForm
from wtforms import (StringField,
                     SubmitField)
from wtforms.validators import InputRequired, Length


class NotifierForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(min=5, max=120, message=('Max 120 digits'))])
    token = StringField('Token', validators=[InputRequired(), Length(max=120, message=('Max 120 digits'))])
    chat_id = StringField('Chat ID', validators=[InputRequired(), Length(max=120, message=('Max 120 digits'))])

    submit = SubmitField('Insert')


class EditNotifierForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(min=5, max=120, message=('Max 120 digits'))])
    token = StringField('Token', validators=[InputRequired(), Length(max=120, message=('Max 120 digits'))])
    chat_id = StringField('Chat ID', validators=[InputRequired(), Length(max=120, message=('Max 120 digits'))])

    submit = SubmitField('Confirm')
