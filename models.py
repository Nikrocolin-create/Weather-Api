from app import db
from datetime import datetime


class ApiRequests(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(64))
    updated = db.Column(db.String(64))
    sky = db.Column(db.String(20))
    temperature = db.Column(db.String(64))
    pressure = db.Column(db.String(64))
    humidity = db.Column(db.String(64))
