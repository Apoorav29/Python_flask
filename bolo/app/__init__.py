# Import flask and template operators
from flask import *

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

from functools import wraps
# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = '/home/alirizwi/it_Major/it_mm/boilerplate/app/static/uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['bmp', 'png', 'jpg', 'jpeg', 'gif'])

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

from app.user.models import User
from app.photos.models import Photo
from app.albums.models import Album
from app.mapp_photos.models import Mapp_Photos
from app.share_photos.models import Share_Photos

# Sample HTTP error handling
# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
   return render_template('index.html'), 200

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify(message="Unauthorized", success=False), 401
        return f(*args, **kwargs)
    return decorated

# Import a module / component using its blueprint handler variable (mod_auth)
from app.user.controllers import mod_user
#from app.todo.controllers import mod_todo

# Register blueprint(s)
app.register_blueprint(mod_user)
#app.register_blueprint(mod_todo)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
