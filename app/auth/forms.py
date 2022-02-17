import email
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError,BooleanField
from  wtforms.validators import InputRequired, Email,EqualTo,Length,Regexp
from ..models import Users


class RegisterForm(FlaskForm):
    username = StringField(' Preferred Username e.g. Mishael', validators=[
                                                                            InputRequired(),
                                                                            Length(min=3,max=40),
                                                                            Regexp('^\w+$',0, 'Usernames should have only be alphanumeric,periods or underscores'),
                                                                            ])
    email = StringField('Please enter your email here', validators=[InputRequired(),Email()])
    password = PasswordField('Enter your Password',validators = [
                                                                    InputRequired(), 
                                                                    EqualTo('password_confirm',message = 'Passwords Must match, Try again'),
                                                                    Length(min=5,max=32)])
    password_confirm = PasswordField('Confirm Password',validators = [InputRequired()])
    submit = SubmitField('Sign Up')
    
    def email_validate(self, mail_field):
        if  Users.query.filter_by(email= mail_field.data).first():
            raise ValidationError('Email already taken, Try another email')

    def username_validate(self,u_field):
        if Users.query.filter_by(username=u_field.data).first():
            raise ValidationError('That username is taken!!,Try new one')
class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[InputRequired(),Email()])
    password = PasswordField('Password',validators =[InputRequired()])
    remember = BooleanField('Keep me logged in')
    submit = SubmitField('Login')            

            
            