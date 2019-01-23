from flask import Flask, Blueprint
app = Flask(__name__)
app.config['SECRET_KEY'] = "coding is cool"

from api.views.users_views import users_blueprint
app.register_blueprint(users_blueprint)

from api.views.incidents_views import incidents_blueprint
app.register_blueprint(incidents_blueprint)
