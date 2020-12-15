from flask_wtf import FlaskForm
from wtforms import (StringField,
                     PasswordField,
                     IntegerField,
                     SubmitField,
                     BooleanField,
                     SelectField)
from wtforms.validators import InputRequired, Length, ValidationError
from appi2c.ext.mqtt.mqtt_models import ClientMqtt
from appi2c.ext.device.device_forms import Device


def validator_topic_not_imput(form, field):
    if len(field.data) > 0:
        if len(field.data) > 120:
            raise ValidationError('Max 120 digits')
        if '/' not in field.data:
            raise ValidationError('Invalid topic')
    else:
        pass


class MqttClientForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(max=60, message=('Max 60 digits'))])
    address_url = StringField('URL', validators=[InputRequired(), Length(max=120, message=('Max 120 digits'))])
    port = IntegerField('Port', validators=[InputRequired()])
    username = StringField('Username', validators=[Length(max=20, message=('Max 20 digts'))])
    password = PasswordField('Password', validators=[Length(max=20, message=('Max 20 digts'))])
    keep_alive = IntegerField('Keep Alive')

    last_will_topic = StringField('Last Will Topic', validators=[validator_topic_not_imput])
    last_will_message = StringField('Last Will Message', validators=[Length(max=120, message=('Max 120 digits'))])
    last_will_qos = SelectField("Last Will Qos", choices=[(0, 0), (1, 1), (2, 2)], default=0)
    last_will_retain = SelectField('Last Will Retain', choices=[(False, False), (True, True)], default=False)

    status = BooleanField('Status')
    submit = SubmitField('Insert')

    def validate_name(self, name):
        client = ClientMqtt.query.filter_by(name=name.data.title()).first()
        if client is not None:
            raise ValidationError('Please use a different broker name.')


class EditMqttForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(max=60, message=('Max 60 digits'))])
    address_url = StringField('URL', validators=[InputRequired(), Length(max=120, message=('Max 120 digits'))])
    port = IntegerField('Port', validators=[InputRequired()])
    username = StringField('Username', validators=[Length(max=20, message=('Max 20 digts'))])
    password = PasswordField('Password', validators=[Length(max=20, message=('Max 20 digts'))])
    keep_alive = IntegerField('Keep Alive')

    last_will_topic = StringField('Last Will Topic', validators=[validator_topic_not_imput])
    last_will_message = StringField('Last Will Message', validators=[Length(min=5 , max=120, message=('Min 5 and Max 120 digits'))])
    last_will_qos = SelectField("Last Will Qos", choices=[(0, 0), (1, 1), (2, 2)], default=0)
    last_will_retain = SelectField('Last Will Retain', choices=[(False, False), (True, True)], default=False)

    status = BooleanField('Status')
    submit = SubmitField('Confirm')


