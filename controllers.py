from datetime import datetime
from flask import request, make_response, render_template
from Core.Parser import Parser
import requests
from app import db
from config import API_KEY
from models import ApiRequests


class BaseController:
    def __init__(self):
        self.request = request

    def call(self, *args, **kwds):
        try:
            return self._call(*args, **kwds)
        except Exception as ex:
            return make_response(str(ex), 500)

    def _call(self, *args, **kwds):
        raise NotImplementedError("_call")


class ResultMaker(BaseController):
    def _call(self, city):
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}")
        if not response.ok:
            return "not_found"
        parsed = Parser().parse(response.json())
        obj = ApiRequests(city=parsed['city'], sky=parsed['sky'],
                    temperature=parsed['temperature'], pressure=parsed['pressure'],
                    humidity=parsed['humidity'], windspeed=parsed['windspeed'],
                    updated=datetime.strptime(parsed['updated'], '%Y-%m-%d %H:%M:%S'))
        db.session.add(obj)
        db.session.commit()
        self.weather = {"city" : parsed['city'], 'sky': parsed['sky'],
                    'temperature': parsed['temperature'], 'pressure': parsed['pressure'],
                    'windspeed': parsed['windspeed'],
                    'humidity': parsed['humidity']}
        return parsed

    def clothes(self):
        self.clothes = {}
        if self.weather['temperature'] > 298:
            self.clothes['body'] = 'T-shirt'
        elif self.weather['temperature'] > 293:
            self.clothes['body'] = 'Longsleeve'
        elif self.weather['temperature'] > 288:
            self.clothes['body'] = 'Light jacket and T-shirt'
        elif self.weather['temperature'] > 283:
            self.clothes['body'] = 'Jacket'
        elif self.weather['temperature'] > 273:
            self.clothes['body'] = 'Coat'
        elif self.weather['temperature']:
            self.clothes['body'] = 'Coat and sweater'

        if self.weather['temperature'] > 298:
            self.clothes['legs'] = 'Shorts or skirt'
        elif self.weather['temperature'] > 288:
            self.clothes['legs'] = 'Light trousers or jeans'
        elif self.weather['temperature'] > 278:
            self.clothes['legs'] = 'trousers or jeans'
        elif self.weather['temperature']:
            self.clothes['legs'] = 'Warm trousers or warm jeans'

        if self.weather['temperature'] > 298:
            self.clothes['feet'] = 'Sandals'
        elif self.weather['temperature'] > 286:
            self.clothes['feet'] = 'Snickers or shoes'
        elif self.weather['temperature'] > 278:
            self.clothes['feet'] = 'Boots'
        elif self.weather['temperature']:
            self.clothes['feet'] = 'Warm boots'

        if self.weather['temperature'] > 298:
            self.clothes['head'] = 'Cap'
        elif self.weather['temperature'] < 283:
            self.clothes['head'] = 'Hat'

        if self.weather['sky'] == "clear" and self.weather['temperature'] >= 298:
            self.clothes['accessories'] = 'sunglasses'
        if self.weather['humidity'] > 75:
            self.clothes['accessories'] = 'umbrella'
        return self.clothes

if __name__ == "__main__":
    print("hello")
    response = ResultMaker().call('Moscow')
    print(response)