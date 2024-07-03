from flask import Flask
from pymongo import MongoClient
import os

db = None

def create_app():
    app = Flask(__name__)

    client = MongoClient(os.getenv('MONGODB_URI', 'mongodb://mongo:27017'))
    
    global db
    db = client[os.getenv('MONGODB_DB', 'CrudApp')]

    print(db)

    from .api import api
    app.register_blueprint(api)

    @app.route('/')
    def index():
        return 'Hello there!'



    return app