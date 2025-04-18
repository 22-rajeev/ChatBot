from flask_wtf import FlaskForm
from wtforms import StringField ,PasswordField ,SubmitField
from wtforms.validators import DataRequired , Length , Email ,EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username' ,validators=[DataRequired(),Length(min=2 ,max=15),])
    email = StringField('Email' , validators=[DataRequired() , Email()])
    password = PasswordField('Password' , validators=[DataRequired() ,Length(min=6 ,max=10)])
    confirm_password = PasswordField('Confirm Password' , validators=[DataRequired() ,EqualTo('password')])
    submit = SubmitField('Sign Up')



class LoginForm(FlaskForm):
    email = StringField('Email' , validators=[DataRequired() , Email()])
    password = PasswordField('Password' , validators=[DataRequired()])
    submit = SubmitField('Login')

