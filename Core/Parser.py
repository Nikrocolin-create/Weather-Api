from datetime import datetime

class Parser():
    def parse(self, response_json):
        dict_res = {"sky": response_json['weather'][0]['main'],
                    "temperature": int(response_json['main']['temp']),
                    "pressure": response_json['main']['pressure'],
                    "humidity": response_json['main']['humidity'],
                    "city": response_json['name'],
                    "updated": str(datetime.now())[:-7]}
        return dict_res





#
#
#
#