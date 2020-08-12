from datetime import datetime
from app import db
from models import ApiRequests

if __name__=="__main__":
    str1 = "2020-08-12 08:30:23"
    obj1 = ApiRequests(city="Moscow", sky="Clean",
                    temperature="290", pressure="100",
                    humidity="50", updated=datetime.strptime(str1, '%Y-%m-%d %H:%M:%S'))
    db.session.add(obj1)
    db.session.commit()
