"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from DemoFormProject import app
from DemoFormProject.Models.LocalDatabaseRoutines import create_LocalDatabaseServiceRoutines


from datetime import datetime
from flask import render_template, redirect, request

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import json 
import requests

import io
import base64

from os import path

from flask   import Flask, render_template, flash, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms import TextField, TextAreaField, SubmitField, SelectField, DateField
from wtforms import ValidationError


from DemoFormProject.Models.QueryFormStructure import QueryFormStructure 
from DemoFormProject.Models.QueryFormStructure import LoginFormStructure 
from DemoFormProject.Models.QueryFormStructure import UserRegistrationFormStructure 

###from DemoFormProject.Models.LocalDatabaseRoutines import IsUserExist, IsLoginGood, AddNewUser 

db_Functions = create_LocalDatabaseServiceRoutines() 


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

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


@app.route('/Album')
def Album():
    """Renders the about page."""
    return render_template(
        'PictureAlbum.html',
        title='Presidents Photo Album',
        year=datetime.now().year,
        message='Welcome to my photo album'
    )


@app.route('/Query', methods=['GET', 'POST'])
def Query():

    Name = None
    Country = ''
    capital = ''
    df = pd.read_csv(path.join(path.dirname(__file__), 'static\\Data\\capitals.csv'))
    df = df.set_index('Country')

    raw_data_table = df.to_html(classes = 'table table-hover')

    form = QueryFormStructure(request.form)
     
    if (request.method == 'POST' ):
        name = form.name.data
        Country = name
        if (name in df.index):
            capital = df.loc[name,'Capital']
            raw_data_table = ""
        else:
            capital = name + ', no such country'
        form.name.data = ''



    return render_template('Query.html', 
            form = form, 
            name = capital, 
            Country = Country,
            raw_data_table = raw_data_table,
            title='Query by the user',
            year=datetime.now().year,
            message='This page will use the web forms to get user input'
        )

# -------------------------------------------------------
# Register new user page
# -------------------------------------------------------
@app.route('/register', methods=['GET', 'POST'])
def Register():
    form = UserRegistrationFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (not db_Functions.IsUserExist(form.username.data)):
            db_Functions.AddNewUser(form)
            db_table = ""

            flash('Thanks for registering new user - '+ form.FirstName.data + " " + form.LastName.data )
            # Here you should put what to do (or were to go) if registration was good
        else:
            flash('Error: User with this Username already exist ! - '+ form.username.data)
            form = UserRegistrationFormStructure(request.form)

    return render_template(
        'register.html', 
        form=form, 
        title='Register New User',
        year=datetime.now().year,
        repository_name='Pandas',
        )

# -------------------------------------------------------
# Login page
# This page is the filter before the data analysis
# -------------------------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def Login():
    form = LoginFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        print(form.username.data)
        print(form.password.data)
        if (db_Functions.IsLoginGood(form.username.data, form.password.data)):
            flash('Login approved!')
            #return redirect('<were to go if login is good!')
        else:
            flash('Error in - Username and/or password')
   
    return render_template(
        'login.html', 
        form=form, 
        title='Login To Data Analysis',
        year=datetime.now().year,
        repository_name='Pandas',
        )



@app.route('/DataModel')
def DataModel():
    """Renders the contact page."""
    return render_template(
        'DataModel.html',
        title='This is my data model page',
        year=datetime.now().year,
        message='In this page you will be able to see my data sets'
    )


@app.route('/DataSet1')
def DataSet1():

    df = pd.read_csv(path.join(path.dirname(__file__), 'static\\Data\\BL.csv'))
    raw_data_table = df.to_html(classes = 'table table-hover')


    """Renders the contact page."""
    return render_template(
        'DataSet1.html',
        title='This is Data Set Bill Clinton page',
        raw_data_table = raw_data_table,
        year=datetime.now().year,
        message='In this page we will display the datasets'
    )

@app.route('/DataSet2')
def DataSet2():

    df = pd.read_csv(path.join(path.dirname(__file__), 'static\\Data\\BA.csv'))
    raw_data_table = df.to_html(classes = 'table table-hover')


    """Renders the contact page."""
    return render_template(
        'DataSet2.html',
        title='This is Data Set Barack Obama page',
        raw_data_table = raw_data_table,
        year=datetime.now().year,
        message='In this page we will display the datasets'
    )

@app.route('/DataSet3')
def DataSet3():

    df = pd.read_csv(path.join(path.dirname(__file__), 'static\\Data\\GB.csv'))
    raw_data_table = df.to_html(classes = 'table table-hover')


    """Renders the contact page."""
    return render_template(
        'DataSet3.html',
        title='This is Data Set George Bush page',
        raw_data_table = raw_data_table,
        year=datetime.now().year,
        message='In this page we will display the datasets'
    )

@app.route('/DataSet4')
def DataSet4():

    df = pd.read_csv(path.join(path.dirname(__file__), 'static\\Data\\DT.csv'))
    raw_data_table = df.to_html(classes = 'table table-hover')


    """Renders the contact page."""
    return render_template(
        'DataSet4.html',
        title='This is Data Set Donald Trump page',
        raw_data_table = raw_data_table,
        year=datetime.now().year,
        message='In this page we will display the datasets'
    )


