from flask import Flask, jsonify, abort, request, url_for
import datetime
import time
from random import randint
from mongoengine import connect, StringField, IntField, DateTimeField, Document
import json
import os

#---hw3 settings---
#connect(db="hw4-Activity", host="localhost")
#-----

#---hw6 mlab---
mlab_host = os.environ.get('DB_HOST')
mlab_db = os.environ.get('DB')
mlab_user = os.environ.get('DB_USER')
mlab_password = os.environ.get('DB_PASSWORD')

connect(db=mlab_db,
	host=mlab_host,
	username=mlab_user,
	password=mlab_password)

#---hw7 redis & celery, using HEROKU---
sleep_time = os.environ.get('SLEEP_TIME', default=0)

app = Flask(__name__)

class activityLog(Document):
	ID = StringField()
	user_id = IntField(required=True)
	username = StringField(required=True, max_length=64)
	timestamp = DateTimeField(default=datetime.datetime.utcnow)
	details = StringField(required=True)
	location = StringField()

#create 10 log records for method GET
#activity = activityLog(
#	user_id = 1,
#	username = "Testing",
#	timestamp = datetime.datetime.now(),
#	details = "Clicking around",
#)

#activity.save()

#search objects
#print(activityLog.objects.get(id = "5bccbe4a07612910d2ab1ede"))


#comment out hw3 code sections
#activity_log = [
#	{
#		'id': 0,
#		'user_id': 1,
#		'username': 'john',
#		'timestamp': datetime.utcnow(),
#		'details': "Important stuff here",
#	},
#	{
#		'id': 1,
#		'user_id': 2,
#		'username': 'yoko',
#		'timestamp': datetime.utcnow(),
#		'details': "Even more important",
#	},
#	{
#		'id': 2,
#		'user_id': 9999,
#		'username': 'tester',
#		'timestamp': datetime.utcnow(),
#		'details': "helllooooooooo"
#	}	
#]


#data = {"user_id" : "123", "username" : "testingman", "details" : "testing 123 abc"}
#doc = activityLog(**data)
#doc.save()

#---- convert the database object to json, then json -> dict------
activityData = activityLog.objects()
json_data = activityData.to_json()
activityDatas = json.loads(json_data)


#print(activityDatas)
#for oid in activityDatas:
	#print(oid)
	#print(oid["_id"]["$oid"])


#convert to json
def getID(requestData):
	#requestData1 = requestData.objects
	json_id = requestData.to_json()
	id_location = json.loads(json_id)
	return id_location


#----
#convertion function for search by id : database object -> dict
def convertDict(dataInput):
	obj_json = dataInput.to_json()
	obj_dict = json.loads(obj_json)
	return obj_dict
#jsonQ = convertDict(activityLog.objects.get(id = "5bcc17790761290a9c6ec29d"))



@app.route("/")
def hello():
	return ("Testing API")

#return result by ...
@app.route("/api/activities/<string:oid>", methods=["GET"])
def activity(oid):
	#if id is less than 0 or id is greater than the hex length, throw error
	if (len(oid) < 24 or len(oid) > 24):
		abort(404)
	
	resultJson = convertDict(activityLog.objects.get(id = oid))
	return jsonify(resultJson)




#get 10 recent logs
@app.route("/api/activities/", methods=["GET"])
def activities():
	#return jsonify(activityDatas[0:10])
	return jsonify(activityDatas)

#send a message thru api
@app.route("/api/activities/", methods=["POST"])
def activites_add():
	
	#check if it's json or not
	if not request.json:
		abort(400)

	postData = activityLog(
		user_id=request.json["user_id"],
		username=request.json["username"],
		timestamp=request.json["timestamp"],
		details=request.json["details"],
	)
	
	#save to database
	postData.save()	
	
	
	#add location into the document and save&update the database
	locationID = postData['id']
	postData["ID"] = str(locationID)
	postData["location"] = "/api/activities/" + str(locationID)
	postData.save()	
	time.sleep(int(sleep_time))


	#return 201 on success
	return jsonify(getID(postData)), 201
