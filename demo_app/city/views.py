from flask import Flask, render_template, Blueprint
from demo_app.city.models import City
city = Blueprint("city", __name__)

@city.route('/cities')
def cities():
    cities = City.query.all()
    print(cities.__dict__)
    return render_template("products.html",
                           title="Products",
                           products=products)