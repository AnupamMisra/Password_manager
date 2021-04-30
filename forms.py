from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, URL, AnyOf


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',  validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    password = PasswordField('You know what to write', validators=[DataRequired()])
    submit = SubmitField('Login')

class Newcredentialssetup(FlaskForm):
    website = StringField('Website name', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Set')   

class Get_passwordform(FlaskForm):
    web = StringField('Website name', validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField('Get')   

class reset_credsform(FlaskForm):

    answer = StringField('Answer security question', validators=[DataRequired(), Length(min=2, max=200)])
    otp = IntegerField('Enter OTP from your phone', validators=[DataRequired()])
    website = StringField('Website name', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Reset') 

class securityques(FlaskForm):
    answer = StringField('Answer security question', validators=[DataRequired(), Length(min=2, max=200)])
    otp = IntegerField('Enter OTP from your phone', validators=[DataRequired()])
    p = PasswordField('New password', validators=[DataRequired()])
    p2 = PasswordField('Confim password', validators=[DataRequired(),EqualTo('p')])
    submit = SubmitField('Enter') 
