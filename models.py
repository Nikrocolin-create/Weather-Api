from app import db


class ApiRequests(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(64))
    windspeed = db.Column(db.Integer)
    sky = db.Column(db.String(30))
    temperature = db.Column(db.Integer)
    pressure = db.Column(db.Integer)
    humidity = db.Column(db.Integer)
    updated = db.Column(db.DateTime)