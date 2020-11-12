from flask import Flask, Blueprint

from .city.models import db
from .city.views import city

app = Flask(__name__)
#app.config.from_object('config')


# Add the `constants` variable to all Jinja templates.
# @app.context_processor
# def provide_constants():
#     return {"constants": {"TUTORIAL_PART": 1}}

db.init_app(app)

app.register_blueprint(city)