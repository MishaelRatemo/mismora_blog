from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField,TextAreaField, ValidationError
from wtforms.validators import Regexp,Length,Email,InputRequired
from ..models import Users, Comments,Posts

class PostsForm(FlaskForm):
    post_title = StringField('Post Title', validators=[InputRequired()])
    body = StringField("Tell us what's on your mind?...", validators=[InputRequired()])
    submit = SubmitField('Submit')
class CommentForm(FlaskForm):
    body = StringField("Enter your comment", validators=[InputRequired()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Your bio goes heere.',validators = [InputRequired()])
    submit = SubmitField('Submit')