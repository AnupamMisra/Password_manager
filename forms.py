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
    password = PasswordField('What was the keyphrase given to you', validators=[DataRequired()])
    submit = SubmitField('Login')

class Newcredentialssetup(FlaskForm):
    website = StringField('Website', validators=[DataRequired(), Length(min=2, max=20)])
    URL = StringField('url', validators=[DataRequired()]) #URL validation required later
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    pwd_choice = IntegerField('Password setup choice', validators=[AnyOf([1,2])])
    p = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Set')   

class Get_passwordform(FlaskForm):
    web = StringField('Website name', validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField('Get')   

class reset_credsform(FlaskForm):

    answer = StringField('Answer security question', validators=[DataRequired(), Length(min=2, max=200)])
    otp = IntegerFieldField('Enter OTP', validators=[DataRequired(), Length(min=2, max=200)])
    website = StringField('Website', validators=[DataRequired(), Length(min=2, max=20)])
    URL = StringField('url', validators=[DataRequired()]) #URL validation required later
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    pwd_choice = IntegerField('Password setup choice', validators=[DataRequired(),AnyOf([1,2])])
    p = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Reset') 

class securityques(FlaskForm):
    answer = StringField('Answer security question', validators=[DataRequired(), Length(min=2, max=200)])
    otp = IntegerFieldField('Enter OTP', validators=[DataRequired(), Length(min=2, max=200)])
    p = PasswordField('Password', validators=[DataRequired()])
    p2 = PasswordField('Password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Enter') 
