from flask import Flask, jsonify, abort, request, url_for
from datetime import datetime
from random import randint
from mongoengine import connect, StringField, IntField, Document
import json
connect(db="hw4-Activity", host="localhost")

app = Flask(__name__)

class activityLog(Document):
	user_id = IntField(required=True)
	username = StringField(required=True, max_length=64)
	details = StringField(required=True)

#create 10 log records for method GET
activity = activityLog(
	user_id = 999,
	username = "test9",
	details = "9walking around",
)

activity.save()

#print(activityLog.objects.get(&oumloid = "5bccbe4a07612910d2ab1ede"))


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


#---
#activity.save()


#for activity1 in activityLog.objects:
#	print(activity1.details)

#print({'activityLog' : activityLog.objects[0:4]})




#data = {"user_id" : "123", "username" : "research", "details" : "Statistical analysis"}
#doc = activityLog(**data)
#doc.save()

#---- convert the database object to json, then json -> dict------
activityData = activityLog.objects()
json_data = activityData.to_json()
activityDatas = json.loads(json_data)


#print(activityDatas)
for oid in activityDatas:
	#print(oid)
	print(oid["_id"]["$oid"])



def getID(requestData):
	#requestData1 = requestData.objects
	json_id = requestData.to_json()
	id_location = json.loads(json_id)
	return id_location

@app.route("/")
def hello():
	return ("Testing API")

@app.route("/api/activities/<id>", methods=["GET"])
def activity(id):
	#if id is less than 0 or id is greater than the length, throw error
	#if id < 0 or id >= len(activityDatas):
	#	abort(404)
	
	#search the database
	
	return 1

#get all activities log
@app.route("/api/activities/", methods=["GET"])
def activities():
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
		details=request.json["details"],
	)
	postData.save()	
	
	#check if sucessful
	
	testing1 = json.dumps(getID(postData))
	print(type(testing1))

	print(testing1["_id"]["$oid"])
	#return id location	
	return jsonify(getID(postData))



