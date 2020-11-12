try:
    from .config import db
except ImportError:
    from config import db
# from flask import current_app as app

# db = app.config['db']

class City(db.Model):
    __tablename__ = "city"
    city_id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(1024))
    start_date = db.Column(db.String(32))
    end_date = db.Column(db.String(32))
    price = db.Column(db.String(1024))
    status = db.Column(db.String(32))
    color = db.Column(db.String(32))


# class CitySchema(ma.ModelSchema):
#     class Meta:
#         model = City
#         sqla_session = db.session



