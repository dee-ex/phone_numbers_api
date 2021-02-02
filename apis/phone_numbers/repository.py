from phone_numbers import db

from apis.entities.phone_numbers import PhoneNumberEntity

class PhoneNumberRepository:
    def create(self, phone_number):
        db.session.add(phone_number)
        db.session.commit()

        return phone_number

    def get_list(self, offset=0, limit=10):
      return PhoneNumberEntity.query.limit(limit).offset(offset).all()

    def get(self, id):
      phone_number = PhoneNumberEntity.query.get(id)
      return phone_number

    def update_name(self, id, name):
      phone_number = PhoneNumberEntity.query.get(id)
      phone_number.name = name

      db.session.commit()

    def update_num(self, id, num):
      phone_number = PhoneNumberEntity.query.get(id)
      phone_number.num = num

      db.session.commit()

    def update_subnum(self, id, subnum):
      phone_number = PhoneNumberEntity.query.get(id)
      phone_number.subnum = subnum

      db.session.commit()
    def update_note(self, id, note):
      phone_number = PhoneNumberEntity.query.get(id)
      phone_number.note = note

      db.session.commit()

    def delete(self, id):
      phone_number = PhoneNumberEntity.query.get(id)

      db.session.delete(phone_number)
      db.session.commit()
