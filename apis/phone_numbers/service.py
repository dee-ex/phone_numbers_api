from phone_numbers import db

from apis.entities.phone_numbers import PhoneNumberEntity

class PhoneNumberService:
    def __init__(self, repo):
        self.repo = repo

    def create(self, data):
        new_phone_number = PhoneNumberEntity(name=data["name"], num=data["num"], subnum=data["subnum"], note=data["note"])

        return self.repo.create(new_phone_number)

    def get_list(self, offset=0, limit=10):
      return self.repo.get_list(offset=offset, limit=limit)

    def get(self, id):
      res = self.repo.get(id)
      if res == None:
        raise ValueError("Id not found")

      return res

    def update(self, id, data):
      if "name" in data:
        self.repo.update_name(id, data["name"])
      if "num" in data:
        self.repo.update_num(id, data["num"])
      if "subnum" in data:
        self.repo.update_subnum(id, data["subnum"])
      if "note" in data:
        self.repo.update_note(id, data["note"])

    def delete(self, id):
      self.repo.delete(id)
