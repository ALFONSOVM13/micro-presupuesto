from flask import Flask, jsonify, request
from utils.constants import Settings
from database.database import get_db
from flask_migrate import Migrate
from routes import register_routes
from database.connection import db
import models

app = Flask(__name__)
migrate = Migrate(app, db)
register_routes(app)


@app.before_request
def before_request():
    with get_db() as db:
        request.db = db


@app.route('/')
def index():
    return jsonify({"data":"Hello World, this api is the inventory api!"} ), 200

if __name__ == '__main__':
    print("Starting server...")
    print(Settings.DEBUG)
    print(type(Settings.DEBUG))
    print(bool(Settings.DEBUG))
    app.run(host=Settings.HOST, port=Settings.PORT, debug=bool(Settings.DEBUG))