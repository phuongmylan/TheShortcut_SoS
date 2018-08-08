from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
from flask_uploads import UploadSet, configure_uploads, IMAGES

db = SQLAlchemy()
login_manager = LoginManager()
bootstrap = Bootstrap()
bcrypt = Bcrypt()
photos = UploadSet('photos', IMAGES)

def create_app(config_type):
    app = Flask(__name__)

    configuration = os.path.join(os.getcwd(),'config',config_type+'.py')
    app.config.from_pyfile(configuration)
    configure_uploads(app, photos)

    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)
    bcrypt.init_app(app)

    from app.courses import crs
    app.register_blueprint(crs)

    return app
