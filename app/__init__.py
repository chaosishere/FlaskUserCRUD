from flask import Flask
from pymongo import MongoClient

db = None

def create_app():
    app = Flask(__name__)

    client = MongoClient('mongodb+srv://shendgepratham4:jq5BucX1VcuI5yM1@crudapp.l3nsvv8.mongodb.net/?retryWrites=true&w=majority&appName=CrudApp')
    
    global db
    db = client.CrudApp

    print(db)

    from .api import api
    app.register_blueprint(api)

    @app.route('/')
    def index():
        return 'Hello there!'



    return app