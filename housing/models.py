import datetime
from flask import url_for
from housing import db

class Rent(db.Document):
  created_at = db.DateTimeField(default=datetime.datetime.now, required = True)
  month = db.StringField(required=True)
  year = db.IntField(required=True)
  docType = db.StringField(required=True, default = 'Rent')
  prop_id = db.IntField(required=True)
  nickname = db.StringField(required=True)
  unit = db.StringField(required=True)
  tenant = db.StringField(required=True)
  rent = db.DecimalField(required=True, precision=2)
  paid = db.DecimalField(required=True, precision=2)
  due_date = db.IntField(required=True)
  paid_date = db.IntField(required=True)
  comments = db.StringField(required=True, default = 'No Comment')

class Maintenance(db.Document):
  created_at = db.DateTimeField(default=datetime.datetime.now, required = True)
  month = db.StringField(required=True)
  year = db.IntField(required=True)
  docType = db.StringField(required=True, default = 'Maint')
  date = db.IntField(required=True)
  prop_id = db.IntField(required=True)
  nickname = db.StringField(required=True)
  contractor = db.StringField(required=True)
  labor_cost = db.DecimalField(required=True, default = 0.00, precision=2)
  material_cost = db.DecimalField(required=True, default = 0.00, precision=2)
  paid = db.BooleanField(required = True, default = False)
  comments = db.StringField(required = True, default = 'No Comment')

class Taxes(db.Document):
  created_at = db.DateTimeField(default=datetime.datetime.now, required = True)
  month = db.StringField(required=True)
  year = db.IntField(required=True)
  docType = db.StringField(required=True, default = 'Taxes')
  prop_id = db.IntField(required=True)
  nickname = db.StringField(required=True)
  amount = db.DecimalField(required=True, default = 0.00, precision=2)
  due_date = db.IntField(required=True)
  paid_date = db.IntField(required=True)

class Bills(db.Document):
  created_at = db.DateTimeField(default=datetime.datetime.now, required = True)
  month = db.StringField(required=True)
  year = db.IntField(required=True)
  docType = db.StringField(required=True, default = 'Bills')
  nickname = db.StringField(required=True)
  prop_id = db.IntField(required=True)
  amount = db.DecimalField(required=True, precision=2)
  bill_type = db.StringField(required=True)
  due_date = db.IntField(required=True)
  paid = db.BooleanField(required = True, default = False)
  comments = db.StringField(required = True, default = 'No Comment')