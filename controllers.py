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
        print(response.json())
        if not response.ok:
            return "not_found"
        parsed = Parser().parse(response.json())
        obj = ApiRequests(city=parsed['city'], sky=parsed['sky'],
                    temperature=parsed['temperature'], pressure=parsed['pressure'],
                    humidity=parsed['humidity'],
                    updated=datetime.strptime(parsed['updated'], '%Y-%m-%d %H:%M:%S'))
        db.session.add(obj)
        db.session.commit()
        return parsed

if __name__ == "__main__":
    print("hello")
    response = ResultMaker().call('Moscow11')
    print(response)