# models.py

from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig

db = SQLAlchemy()

class Profile(db.Model):
    __tablename__ = 'profiles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(500), nullable=True)
    other_data = db.Column(db.JSON, nullable=True)

    def __init__(self, id, name, description, image_url, other_data):
        self.id = id
        self.name = name
        self.description = description
        self.image_url = image_url
        self.other_data = other_data

    def __repr__(self):
        return '<Profile %r>' % self.name

def init_app(app):
    # Configure the SQLAlchemy part of the app instance
    app.config['SQLALCHEMY_DATABASE_URI'] = DevelopmentConfig.DATA_WAREHOUSE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize SQLAlchemy here
    db.init_app(app)
