
# Allows us to run a command in the python script
import os


# SQL
import sqlite3
# Flask
# render_template - post the page
# request - Gets form field values
# url_for - link page name
# flash - for error messages
# redirect - loads to another link page
from flask import Flask, render_template, request, url_for, flash, redirect, send_from_directory

# No Page Found
from werkzeug.exceptions import abort

# For upload file
from werkzeug.utils import secure_filename

# For date time
from datetime import date
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'AJqWZcd8YB'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    # Needed to import the models first 
    from models import User
    
    db.init_app(app)
    with app.app_context():
        print('Starting create_all')
        db.create_all()
        print('ending create_all')
    app.app_context().push()
    
    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))
        
    # blueprint for auth routes in our app
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app