
from flask import request, make_response, render_template
from Core.Parser import Parser
import requests
from config import API_KEY


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
        print(city)
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}").json()
        parsed = Parser().parse(response)
        return parsed

if __name__ == "__main__":
    response = ResultMaker().call('Moscow')
    print(response)