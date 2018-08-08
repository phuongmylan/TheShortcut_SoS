from app.courses import crs
from flask import render_template

@crs.route('/')
def home():
    return render_template('template.html')

@crs.route('/detail')
def schedule():
    return render_template('businesstrack.html')
