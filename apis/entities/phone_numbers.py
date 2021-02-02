from phone_numbers import db

# more at: https://docs.sqlalchemy.org/en/13/core/type_basics.html
class PhoneNumberEntity(db.Model):
    __tablename__ = 'phone_numbers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    num = db.Column(db.String(255))
    subnum = db.Column(db.String(255))
    note = db.Column(db.String(255))
 