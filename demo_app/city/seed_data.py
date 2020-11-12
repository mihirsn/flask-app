import os
import json
from config import db
from models import City

# Data to initialize database with
with open('/opt/data.json', 'r') as file:
    city_data = file.read()

city_data_json = json.loads(city_data)

# Delete database file if it exists currently
if os.path.exists('city.db'):
    os.remove('city.db')

# Create the database
db.create_all()

for city in city_data_json:
    c = City(city_id=city['id'], city_name=city['city'], start_date=city['start_date'], end_date=city['end_date'], price=city['price'], status=city['status'], color=city['color'])
    db.session.add(c)

db.session.commit()