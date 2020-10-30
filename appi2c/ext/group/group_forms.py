from flask_wtf import FlaskForm
from wtforms.widgets import TextArea
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError
from appi2c.ext.group.group_models import Group
 


class GroupForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(max=60, message=('Max 60 digits'))])
    description = StringField('Description', widget=TextArea())
    submit = SubmitField('Register')

    def validate_name(self, name):
        group = Group.query.filter_by(name=name.data.title()).first()
        if group is not None:
            raise ValidationError('Please use a different group name.')


class EditGroupForm(FlaskForm):
    id = IntegerField('id')
    name = StringField('Name', validators=[InputRequired(), Length(max=60, message=('Max 60 digits'))])
    description = StringField('Description', widget=TextArea())
    submit = SubmitField('Confirm')


    def validate_name(self, name, id):
        group = Group.query.filter_by(name=name.data.title()).first()
        if group is not None and id != group.id:
            raise ValidationError('Please use a different group name.')


