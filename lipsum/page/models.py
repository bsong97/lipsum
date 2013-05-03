from google.appengine.ext import db

class Message(db.Model):
    content = db.TextProperty(required=True)
    when = db.DateTimeProperty(auto_now_add = True)
