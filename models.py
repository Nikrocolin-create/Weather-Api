from app import db
from datetime import datetime


class ApiRequests(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(64))
    updated = db.Column(db.DateTime, default=datetime.utcnow)
    sky = db.Column(db.String(20))
    temperature = db.Column(db.Float)
    pressure = db.Column(db.Float)
    humidity = db.Column(db.Float)
