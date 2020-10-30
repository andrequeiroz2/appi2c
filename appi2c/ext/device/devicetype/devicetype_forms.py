from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Length


class TypeSwitch(FlaskForm):
    on = StringField('On', validators=[InputRequired(), Length(max=60)], message=('Max 60 digits'))
    off = StringField('Off', validators=[InputRequired(), Length(max=60)], message=('Max 60 digits'))


class TypeSensor(FlaskForm):
    prefix = StringField('Prefix', validators=[Length(max=20)], message=('Max 20 digits'))
    postfix = StringField('Postfix', validators=[Length(max=20)], message=('Max 20 digits'))


class TypeActuator(FlaskForm):
    prefix = StringField('Prefix', validators=[Length(max=20)], message=('Max 20 digits'))
    postfix = StringField('Postfix', validators=[Length(max=20)], message=('Max 20 digits'))
    command = StringField('Command', validators=[Length(max=60)], message=('Max 60 digits'))
