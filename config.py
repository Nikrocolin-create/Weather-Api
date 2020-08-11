import os
basedir = os.path.abspath(os.path.dirname(__file__))
API_KEY = os.environ.get('API_KEY') or "0817225bce6db8df7e8b6047a57914b6"

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    