from flask import render_template
from flask_mail import  Message
from . import mail


def email_message(subject,template,to, **kwargs):
    sender_address= 'pitchershub@gmail.com'
    
    email= Message( subject,sender=sender_address, recipients=[to])
    email.body= render_template(template + '.txt', **kwargs )
    email.html = render_template(template + '.html', **kwargs)
    mail.send(email)