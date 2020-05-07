from flask import Flask
from flask_restful import Api
from database.db import initialize_db
from resources.routes import initialize_routes
import os, json

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app, prefix="/api")
initialize_db(app)
initialize_routes(api)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=6000)