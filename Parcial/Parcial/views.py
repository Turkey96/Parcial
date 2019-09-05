"""
Routes and views for the flask application.
"""

from datetime import datetime
import time
from flask import render_template, request
from Parcial import app
import csv
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )
@app.route('/log', methods=['GET'])
def form():
    now = time.strftime('%d-%m-%Y %H:%M:%S')
    print(now)
    render_template('log.html')
    myFile = open(now+'.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(myData)

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
