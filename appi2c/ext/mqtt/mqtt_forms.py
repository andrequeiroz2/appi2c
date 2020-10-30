from flask_wtf import FlaskForm
from wtforms import (StringField,
                    PasswordField,
                    IntegerField,
                    SubmitField,
                    BooleanField,
                    SelectField)
from wtforms.validators import InputRequired, Length, ValidationError


class MqttClientForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(max=60, message=('Max 60 digits'))])
    address_url = StringField('URL', validators=[InputRequired(), Length(max=120, message=('Max 120 digits'))])
    port = IntegerField('Port', validators=[InputRequired()])
    username = StringField('Username', validators=[Length(max=20, message=('Max 20 digts'))])
    password = PasswordField('Password', validators=[Length(max=20, message=('Max 20 digts'))])
    keep_alive = IntegerField('Keep Alive')

    last_will_topic = StringField('Last Will Topic', validators=[Length(max=120, message=('Max 120 digits'))])
    last_will_message = StringField('Last Will Message', validators=[Length(max=120, message=('Max 120 digits'))])
    last_will_qos = SelectField("Last Will Qos", choices=[(0, 0), (1, 1), (2, 2)], default=0)
    last_will_retain = SelectField('Last Will Retain', choices=[(False, False), (True, True)], default=False)

    status = BooleanField('Status')
    submit = SubmitField('Insert')


class EditMqttForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(max=60, message=('Max 60 digits'))])
    address_url = StringField('URL', validators=[InputRequired(), Length(max=120, message=('Max 120 digits'))])
    port = IntegerField('Port', validators=[InputRequired()])
    username = StringField('Username', validators=[Length(max=20, message=('Max 20 digts'))])
    password = PasswordField('Password', validators=[Length(max=20, message=('Max 20 digts'))])
    keep_alive = IntegerField('Keep Alive')

    last_will_topic = StringField('Last Will Topic', validators=[Length(max=120, message=('Max 120 digits'))])
    last_will_message = StringField('Last Will Message', validators=[Length(max=120, message=('Max 120 digits'))])
    last_will_qos = SelectField("Last Will Qos", choices=[(0, 0), (1, 1), (2, 2)], default=0)
    last_will_retain = SelectField('Last Will Retain', choices=[(False, False), (True, True)], default=False)

    status = BooleanField('Status')
    submit = SubmitField('Confirm')