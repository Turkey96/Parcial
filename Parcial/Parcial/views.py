"""
Routes and views for the flask application.
"""

from datetime import datetime
import pandas as pd
from flask import render_template, request, redirect, url_for, flash
from Parcial import app
import csv
import sqlalchemy as db

#Main function to get database as a pd table
def Database():
    engine = db.create_engine('sqlite:///data.db')

    connection = engine.connect()
    metadata = db.MetaData()

    users = db.Table('data', metadata, autoload=True, autoload_with=engine)
    query = db.select([users])
    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()

    df = pd.DataFrame(ResultSet)
    df.columns = ResultSet[0].keys()
    return df

#Get database table
df=Database()

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )
@app.route('/log', methods=['GET','POST'])
def form():
    if request.method=='GET':
        date=str(datetime.now().strftime("%d_%m_%Y"))
        time=str(datetime.now().time())
        df.insert(3,time,time)
        df.to_csv(date+'.csv',sep=',')
    return(render_template('log.html'))

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