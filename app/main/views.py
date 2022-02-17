
import re
from .. import db
from  flask import render_template,redirect,request,abort,url_for,flash
from ..models import Users,Comments,Posts,Likes,Unlikes
from .forms import UpdateProfile,PostsForm
from flask_login import  login_required, current_user
from . import root
from werkzeug.security import generate_password_hash,check_password_hash
import requests ,json



@root.route('/')
def index():
    title= 'Home Page'
    posts = Posts.query.order_by(Posts.id.desc()).all()
    api_url ='http://quotes.stormconsultancy.co.uk/random.json'
    quotes = requests.get(api_url).json()
    
    return render_template('index.html', title=title, posts=posts, quotes=quotes)


@root.route('/user/<uname>')
def user_profile(uname):
    user = Users.query.filter_by(usernane = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@root.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(name):
    user = Users.query.filter_by(username = name).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@root.route('/post/new/', methods =['GET', 'POST'])
@login_required
def new_post():
    post_form = PostsForm()
    if post_form.validate_on_submit():
        post_title = post_form.post_title .data        
        post_description = post_form.body.data
        user = current_user
        print(current_user._get_current_object().id)
        new_post = Posts(author = current_user , post_title=post_title, post_description= post_description)
        db.session.add(new_post)
        db.session.commit()
        
        return redirect(url_for('root.index'))
    return render_template('posts.html', form= post_form)
        


@root.route('/contact')
def contact():
    
    return render_template('contact.html')    
