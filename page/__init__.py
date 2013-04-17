from flask import Flask
#from flaskext.admin import Admin, BaseView, expose
import settings

app = Flask('page')
app.config.from_object('page.settings')

# Add Admin view here
#admin = Admin(app)


import views
