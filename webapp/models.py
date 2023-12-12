from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# Define the Note model
class Note(db.Model):
    # Note table columns
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# Define the User model, inheriting from UserMixin for Flask-Login integration
class User(db.Model, UserMixin):
    # User table columns
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

    # Relationship with the Note model, establishing a one-to-many relationship
    notes = db.relationship('Note')

