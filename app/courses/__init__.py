from flask import Blueprint

crs = Blueprint('courses', __name__, template_folder='templates', static_folder ='static')

from app.courses import routes
