import unittest
from xml.etree.ElementTree import Comment
from app.models import Comments, Users,Posts



class UserModelTest(unittest.TestCase):
  def setUp(self):
    self.new_user=Users(usernane="ken",email='ken@gmail.com', login_password='ken123')

  def tearDown(self):
    Users.query.delete()
    

  def test_password_setter(self):
    self.assertTrue(self.new_user.login_password is not None)
    
  def test_verify_password(self):
    self.assertTrue(self.new_user.verify_password('ken123'))

  
  def test_unauthorized_access(self):
    with self.assertRaises(AttributeError):
      self.new_user.login_password

  
  def test_save_user(self):
    self.new_user.save_user()
    self.assertTrue(len(Users.query.all())==1)
    
    
    
    
    
    
class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.new_user=Users(usernane="ken",password='123123',role=Users.query.filter_by(username='User').first())
        self.new_post=Posts(category=Posts.query.filter_by(id=1).first(),user=self.new_user)
        self.new_comment=Comments(user=self.new_user,post=self.new_post,post_description='Commenting')


    def tearDown(self):
        Comments.query.delete()
        Posts.query.delete()
        Users.query.delete()


    def test_save_comments(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comments.query.all())==1)
        
        
        

class PostsModelTest(unittest.TestCase):
    def setUp(self):
        self.new_user=Users(username="Mishael",pass_secure='123123',role=Users.query.filter_by(username='User').first())
        self.new_pitch=Posts(category=Posts.query.filter_by(id=1).first(),user=self.new_user)

    def tearDown(self):
        Posts.query.delete()
        Users.query.delete()
        

    def test_check_instance_variables(self):

        self.assertEquals(self.new_post.user,self.new_user)
        self.assertEquals(self.new_pitch.category,Posts.query.filter_by(id=2).first())

    def test_save_pitches(self):
        self.new_user.save_user()
        self.new_post.save_pitch()
        self.assertTrue(len(Posts.query.all())==1)