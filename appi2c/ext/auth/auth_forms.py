from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Length, Email, EqualTo, ValidationError
from appi2c.ext.auth.auth_models import User
from flask_login import current_user


class UserForm(FlaskForm):
    username = StringField('Name', validators=[InputRequired(), Length(min=5, max=20, message=('Min 5 digits and Max 20 digits'))])
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=5, max=20, message=('Min 5 digits and Max 20 digits'))])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    admin = BooleanField('Admin')
    submit = SubmitField('Signup')


    #username is a unique register in user db
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('That username is taken. Please choose a different one.')
        

    #email is a unique register in user db
    def validate_email(self, email):
        email_user = User.query.filter_by(email=email.data).first()
        if email_user is not None:
            raise ValidationError('That email is taken. Please choose a different one.')
            

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(),
                            Length(min=5, max=20, message=('Min 5 digits and Max 20 digts'))])
    password = PasswordField('Password', validators=[InputRequired(),
                              Length(min=5, max=20, message=('Min 5 digits and Max 20 digts'))])
    submit = SubmitField('Login')


class EditProfile(FlaskForm):
    username = StringField('Name', validators=[InputRequired(), Length(min=5 , max=20, message=('Min 5 digits and Max 20 digits'))])
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=5 , max=20, message=('Min 5 digits and Max 20 digits'))])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Confirm')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None and current_user.username != user.username:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user_email = User.query.filter_by(email=email.data).first()
        if user_email is not None and current_user.email != user_email.email:
            raise ValidationError('That username is taken. Please choose a different one.')