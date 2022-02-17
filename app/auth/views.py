from flask import  render_template,request,url_for,redirect, flash
from ..models import Users 
from flask_login import login_user,current_user,login_required,logout_user
from .forms import RegisterForm,LoginForm
from ..email import email_message
from .. import db
from . import auth

@auth.route('/register', methods=['GET', 'POST'])
def register():
    reg_form = RegisterForm()
    if reg_form.validate_on_submit():
        user = Users(user_email=reg_form.email.data,
                     usernane=reg_form.username.data,
                     password=reg_form.password.data
                     )
        db.session.add(user)
        db.session.commit()
        email_message("Welcome to Mismorablog","email/user_welcome",user.user_email,user=user)
        return redirect(url_for('auth.login'))
    title= 'New Account'
    return render_template('auth/register.html', form=reg_form, title=title)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = Users.query.filter_by(user_email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember.data)
            return redirect(request.args.get('next') or url_for('root.index'))
        flash('Invalid username or password. Try again')
    title='Login'
    return render_template('auth/login.html', loginForm=login_form, title=title)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('root.index'))

