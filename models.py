from app import db
from datetime import datetime


class ApiRequests(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(64))
    updated = db.Column(db.DateTime)
    sky = db.Column(db.String(30))
    temperature = db.Column(db.Integer)
    pressure = db.Column(db.Integer)
    humidity = db.Column(db.Integer)
