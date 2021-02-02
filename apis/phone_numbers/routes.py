from phone_numbers import api
from .controller import PhoneNumberResource, PhoneNumberWithIdResource

api.add_resource(PhoneNumberResource, "/phone_numbers")
api.add_resource(PhoneNumberWithIdResource, "/phone_numbers/<int:id>")
