from phone_numbers import ma

class PhoneNumberSchema(ma.Schema):
  class Meta:
    fields = ("id", "name", "num", "subnum", "note" )

class SimplePhoneNumberSchema(ma.Schema):
  class Meta:
    fields = ("id", "name")
