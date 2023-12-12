from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# Initialize SQLAlchemy and set the database file name
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    # Create the Flask application instance
    app = Flask(__name__)

    # Set the secret key for session management
    app.config['SECRET_KEY'] = 'Alexus91'

    # Set the URI for the SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    # Initialize the SQLAlchemy extension with the app
    db.init_app(app)

    # Import blueprints for views and authentication
    from .view import views
    from .auth import auth

    # Register the blueprints with the app
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Import models and create the database tables
    from .models import User, Note
    with app.app_context():
        db.create_all()

    # Initialize Flask-Login extension
    login_manager = LoginManager()

    # Set the login view for redirecting unauthorized users
    login_manager.login_view = 'auth.login'

    # Initialize Flask-Login with the app
    login_manager.init_app(app)

    # Define a function to load a user by their ID for Flask-Login
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    # Create the database if it does not exist
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
