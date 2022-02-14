from . import db
from flask_login import UserMixin, current_user
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class Users( UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column( db.String(255), unique =True, index = True) # email has to unique for every user
    usernane = db.Column(db.String(255))
    login_password = db.Column(db.String(255))
    profile_img_path = db.Column(db.String())
    joined_on = db.Column(db.DateTime(), default=datetime.utcnow)
    user_posts = db.relationship('Post', backref='author', lazy='dynamic')
    user_comments =db.relationship('Comment', backref='author', lazy='dynamic')
    user_like =db.relationship('Like', backref='author', lazy='dynamic')
    user_unlike =db.relationship('Unlike', backref='author', lazy='dynamic')
    
    
    @property
    def password(self):
        raise AttributeError('You are not allowed to read the password attribute')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)# hash password

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password) # check if user passwords march
    
    def __repr__(self):
        return f'{self.username}'   
    
class Posts(db.Model):
    __tablename__= 'posts'
    id = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.String)
    post_description =db.Column(db.Text, index = True)
    post_comments = db.relationship('Comment', backref='post', lazy='dynamic')
    auther_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    @classmethod
    def get_posts(cls, id):
        posts = Posts.query.order_by(pitch_id=id).desc().all()
        return posts
    
    @classmethod    
    def get_user_posts (cls, id):
        user_posts = Posts.query.filter_by(owner_id = id).all()
        return user_posts

    def __repr__(self):
        return f'Post {self.post_description}'
    
class Comments(db.Model):
    __tablename__= 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment_descrip = db.Column(db.Text)
    time_posted = db.Column(db.DateTime,index=True, default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    author_id =db.Column( db.Integer, db.ForeignKey('users.id'))
    
    def __repr__(self):
        return f'Comment: id: {self.id} comment {self.comment_descrip}'
    
class Likes(db.Model):
    __tablename__= 'likes'
    id =db.Column (db.Integer, primary_key=True)
    like =db.Column(db.Integer, default=1)
    post_like_id =db.Column(db.Integer, db.ForeignKey('posts.id'))
    author_id =db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_like(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def add_like(cls,id):
        like = Likes( user = current_user, post_like_id=id)
        like.save_like()
    
    @classmethod
    def get_likes(cls):
        likes = Likes.query.filter_by('id').all()
        return likes

    @classmethod
    def check_user_liked(cls,user_id,post_like_id): 
        '''Chech if user has liked a post() specific'''
        check_like = Likes.query.filter_by(author_id =user_id,post_id=post_like_id)
        return check_like
    
    def __repr__(self):
        return f'{self.author_id}: {self.post_like_id}'
        
    

class Unlikes(db.Model):
    __tablename__= 'unlikes'
    id =db.Column (db.Integer, primary_key=True)
    unlike =db.Column(db.Integer, default=1)
    post_unlike_id =db.Column(db.Integer, db.ForeignKey('posts.id'))
    author_id =db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_unlike(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def add_unlike(cls,id):
        unlike = Unlikes( user = current_user, post_unlike_id=id)
        unlike.save_unlike()
    
    @classmethod
    def get_unlikes(cls):
        unlikes = Unlikes.query.filter_by('id').all()
        return unlikes

    @classmethod
    def check_user_unliked(cls,user_id,post_unlike_id): 
        '''Chech if user has unliked a post() specific'''
        check_unlike = Unlikes.query.filter_by(author_id =user_id,post_id=post_unlike_id)
        return check_unlike
    
    def __repr__(self):
        return f'{self.author_id}: {self.post_unlike_id}'
       
        

    


    