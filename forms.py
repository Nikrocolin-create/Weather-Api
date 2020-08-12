from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class CityForm(FlaskForm):
    city = StringField('Name of the city', validators=[DataRequired()])
    degrees = BooleanField("Celsius degrees")
    submit = SubmitField('find out the forecast')
