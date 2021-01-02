from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError
from appi2c.ext.icon.icon_models import Icon


class IconForm(FlaskForm):
    html_class = StringField('Class Html', validators=[InputRequired(), Length(max=60, message=('Max 60 digits'))])
    submit = SubmitField('Insert')

    def validate_html_class(self, html_class):
        icon = Icon.query.filter_by(html_class=html_class.data.title()).first()
        if icon is not None:
            raise ValidationError('Please use a different icon class.')


class EditIconForm(FlaskForm):
    id = IntegerField('id')
    html_class = StringField('Html Class', validators=[InputRequired(), Length(max=60, message=('Max 60 digits'))])
    submit = SubmitField('Confirm')
