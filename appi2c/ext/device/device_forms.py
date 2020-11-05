from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField
from wtforms.validators import InputRequired, Length, ValidationError
from wtforms_sqlalchemy.fields import QuerySelectField
from appi2c.ext.device.device_models import Device
from appi2c.ext.group.group_controller import choice_query


class DeviceSwitchForm(FlaskForm):
    groups = QuerySelectField(query_factory=choice_query, allow_blank=True, get_label='name', blank_text=u'Select a Group...')
    name = StringField('Name', validators=[InputRequired(), Length(max=60, message=('Max 60 digits'))])
    topic_pub = StringField('Topic Publish', validators=[InputRequired(), Length(max=120, message=('Max 120 digits'))])
    topic_sub = StringField('Topic Subscrib', validators=[Length(max=120, message=('Max 120 digits'))])
    last_will_topic = StringField('Topic Last Will', validators=[Length(max=120, message=('Max 120 digits'))])
    command_on = StringField('On Command', validators=[InputRequired(), Length(max=60, message=('Max 60 digits'))])
    command_off = StringField('Off Command', validators=[InputRequired(), Length(max=60, message=('Max 60 digits'))])
    qos = SelectField("Qos", choices=[(0, 0), (1, 1), (2, 2)], validators=[InputRequired()], default=0)
    retained = SelectField('Retained', choices=[(False, False), (True, True)], default=True)

    submit = SubmitField('Insert')

    def validate_name(self, name):
        device = Device.query.filter_by(name=name.data.title()).first()
        if device is not None:
            raise ValidationError('Please use a different device name.')


class DeviceSensorForm(FlaskForm):
    groups = QuerySelectField(query_factory=choice_query, allow_blank=True, get_label='name', blank_text=u'Select a Group...')
    name = StringField('Name', validators=[InputRequired(), Length(max=60, message=('Max 60 digits'))])
    topic_pub = StringField('Topic Publish', validators=[Length(max=120, message=('Max 120 digits'))])
    topic_sub = StringField('Topic Subscrib', validators=[InputRequired(), Length(max=120, message=('Max 120 digits'))])
    prefix = StringField('Prefix', validators=[Length(max=10, message=('Max 10 digits'))])
    postfix = StringField('Postfix', validators=[Length(max=10, message=('Max 10 digits'))])
    last_will_topic = StringField('Topic Last Will', validators=[Length(max=120, message=('Max 120 digits'))])
    qos = SelectField("Qos", choices=[(0, 0), (1, 1), (2, 2)], validators=[InputRequired()], default=0)
    retained = SelectField('Retained', choices=[('False', 'False'), ('True', 'True')], default='False')

    submit = SubmitField('Insert')

    def validate_name(self, name):
        device = Device.query.filter_by(name=name.data.title()).first()
        if device is not None:
            raise ValidationError('Please use a different device name.')

