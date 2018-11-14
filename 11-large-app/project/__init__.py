# __init__.py under 'project' directory
import os
# from forms import AddForm, DelForm, AddOwnerForm
from flask import Flask, render_template, url_for, \
                    redirect, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd\2_4t#:-y1p9FqrHg0c/n><A9qrb'

################################
##### SQL DATABASE SECTION #####
################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)
