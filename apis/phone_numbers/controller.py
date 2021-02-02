from flask import request
from flask_restful import Resource

from .service import PhoneNumberService
from .repository import PhoneNumberRepository
from apis.schemas.phone_numbers import PhoneNumberSchema, SimplePhoneNumberSchema

class PhoneNumberResource(Resource):
  def __init__(self):
    repo = PhoneNumberRepository()
    self.service = PhoneNumberService(repo)
    self.phone_number_schema = PhoneNumberSchema()
    self.simple_phone_number_schemas = SimplePhoneNumberSchema(many=True)

  def get(self):
    offset = int(request.args.get("offset", 0))
    limit = int(request.args.get("limit", 10))

    try:
      res = self.service.get_list(offset=offset, limit=limit)
    except:
      return {"status": "Error", "message": "Internal Server Error"}, 500
    
    return {"status": "success", "data": self.simple_phone_number_schemas.dump(res)}, 200

  def post(self):
    data = request.get_json()
    try:
      res = self.service.create(data)
    except:
      return {"status": "Error", "message": "Internal Server Error"}, 500

    return {"status": "success", "data": self.phone_number_schema.dump(res)}, 200

class PhoneNumberWithIdResource(Resource):
  def __init__(self):
    repo = PhoneNumberRepository()
    self.service = PhoneNumberService(repo)
    self.phone_number_schema = PhoneNumberSchema()

  def get(self, id):
    try:
      res = self.service.get(id)
    except ValueError as e:
      return {"status": "Error", "message": str(e)}, 404
    except:
      return {"status": "Error", "message": "Internal Server Error"}, 500

    return {"status": "success", "data": self.phone_number_schema.dump(res)}, 200

  def put(self, id):
    # first, we have to check whether id is valid
    try:
      res = self.service.get(id)
    except ValueError as e:
      return {"status": "Error", "message": str(e)}, 404
    except:
      return {"status": "Error", "message": "Internal Server Error"}, 500

    data = request.get_json()
    try:
      self.service.update(id, data)
    except:
      return {"status": "Error", "message": "Internal Server Error"}, 500

    return {"status": "success", "message": "update successfully"}, 200

  def delete(self, id):
    # first, we have to check whether id is valid
    try:
      res = self.service.get(id)
    except ValueError as e:
      return {"status": "Error", "message": str(e)}, 404
    except:
      return {"status": "Error", "message": "Internal Server Error"}, 500

    try:
      self.service.delete(id)
    except:
      return {"status": "Error", "message": "Internal Server Error"}, 500

    return {"status": "success", "message": "delete successfully"}, 200
