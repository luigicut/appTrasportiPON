from mongoengine import *


class tableRow(Document):
    city = StringField(required=False)
    transportCompanies = ListField(required=False, document_type=StringField)
