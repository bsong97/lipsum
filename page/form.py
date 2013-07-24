from flaskext import wtf
from flaskext.wtf import validators

class ContactForm(wtf.Form):
    #title = wtf.TextField('Title', validators=[validators.Required()])
    content = wtf.TextAreaField('Content', validators=[validators.Required("Please enter your message")])
    # Whatever inside Required will be shown if the form is blank when submitted