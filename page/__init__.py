from flask import Flask
#from flaskext.admin import Admin
import settings

app = Flask('page')
#app = Flask(__name__)
app.config.from_object('page.settings') # including CSRF secret key

# Add Admin view here
#admin = Admin(name='my_app')
#admin.init_app(app)


import views
