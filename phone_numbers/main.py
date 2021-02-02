from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

def create_app():
  app = Flask(__name__)

  return app

def init_db(app):
  username = "root"
  password = ""
  host = "localhost"
  dbname = "phone_numbers_api"
  uri = "mysql://" + username + ":" + password + "@" + host + "/" + dbname

  app.config["SQLALCHEMY_DATABASE_URI"] = uri
  db = SQLAlchemy(app)

  return db

def init_ma(app):
  ma = Marshmallow(app)

  return ma

def init_api(app):
  api = Api(app)

  return api


app = create_app()
db = init_db(app)
ma = init_ma(app)
api = init_api(app)
