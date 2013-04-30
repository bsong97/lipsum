from page import app
from models import Message
from decorators import login_required, admin_required

from flask import render_template, flash, url_for, redirect
from flaskext import wtf
from flaskext.wtf import validators

#from google.appengine.api import users
from google.appengine.ext import db

#def message_key(message_name=none):
    #""" Constructs a datastore key for a Messagebook entity with message_name"""
    #return db.Key.from_path('Messagebook', message_name or 'default_messagebook)

class PostForm(wtf.Form):
    #title = wtf.TextField('Title', validators=[validators.Required()])
    content = wtf.TextAreaField('Content', validators=[validators.Required()])
    

@app.route('/')
def redirect_to_home():
    return redirect(url_for('frontpage'))

@app.route('/frontpage')
def frontpage():
    return render_template('frontpage.html')
    
@app.route('/about')
def about():
    return render_template('about.html')
    
@app.route('/projects')
def projects():
    return render_template('projects.html')
    
    
#@app.route('/services')
    #def services():
#    return render_template('services.html')
    
#@app.route('/blog')
    #def blog():
#    return render_template('blog.html')
# Make this into a database

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = PostForm()
    if form.validate_on_submit():
        message = Message(content = form.content.data)
        message.put()
        flash('Thanks, your message has been submitted')
        return redirect(url_for('contact'))
    return render_template('contact.html', form=form)



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    


@app.route('/message')
@login_required
@admin_required
def message():
    """Return the message generated from contact page"""
    messages = db.GqlQuery("SELECT * FROM Message ORDER BY when DESC LIMIT 15")
    return render_template('list_posts.html', messages=messages)
    

