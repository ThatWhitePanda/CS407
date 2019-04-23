#from flask import Flask, jsonify, Response
import os
from mongoengine import *
from datetime import datetime
#from dotenv import load_dotenv

mongo_host = os.getenv('DB_HOST')
mongo_db = os.getenv('DB')
mongo_user = os.getenv('DB_USER')
mongo_password = os.getenv('DB_PASSWORD')

connect(db=mongo_db,
	host=mongo_host,
	username=mongo_user,
	password=mongo_password)

class BusinessProject(Document):
	owner_id = IntField(required=True)
	project_name = StringField(required=True, max_length=64)
	due_date = DateTimeField(default=datetime.utcnow)
	project_details = StringField(required=True)


data = BusinessProject(
	owner_id = 1,
	project_name = 'ABC Project',
	project_details = 'work on this',
)


data.save()

print(data.project_name)
