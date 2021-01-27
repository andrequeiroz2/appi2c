from flask_wtf import FlaskForm
from wtforms.widgets import TextArea
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError
from appi2c.ext.group.group_models import Group
from flask_login import current_user
from wtforms.widgets import HiddenInput


class GroupForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(max=60, message=('Max 60 digits'))])
    description = StringField('Description', widget=TextArea(), validators=[InputRequired()])
    file = FileField('Blue Print', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField('Register')

    def validate_name(self, name):
        group = Group.query.filter_by(name=name.data).filter_by(user_id=current_user.id).first()
        if group is not None:
            raise ValidationError('Please use a different group name.')

    def validate_file(self, file):
        if file.data is None:
            raise ValidationError('Please insert a image.')
        group_file = Group.query.filter_by(file=file.data.filename).filter_by(user_id=current_user.id).first()
        if group_file is not None:
            raise ValidationError('Please use a different file name.')


class EditGroupForm(FlaskForm):
    id = IntegerField(widget=HiddenInput())
    name = StringField('Name', validators=[InputRequired(), Length(max=60, message=('Max 60 digits'))])
    description = StringField('Description', widget=TextArea())  
    file = FileField('Blue Print', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField('Confirm')

    def validate_name(self, name):
        group = Group.query.filter_by(name=name.data).filter_by(user_id=current_user.id).first()
        if group is not None:
            print('Data: ',self.id.data)
            print('Grupo: ',group.id)
            if self.id.data != group.id:
                raise ValidationError('Please use a different group name.')