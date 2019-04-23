from flask import Flask, jsonify, abort, request, url_for
import datetime, time, json
from random import randint
from mongoengine import connect, StringField, IntField, DateTimeField, Document

connect(db="hw4", host="localhost")

app = Flask(__name__)

class activityLogging(Document):
	user_id = IntField(required=True)
	username = StringField(required=True, max_length=64)
	timestamp = StringField
	details = StringField(required=True)

activity = activityLogging(
	user_id = 1,
	username = "developer",
	timestamp = datetime.datetime.now(),
	details = "demo",
)

activity.save()

@app.route("/api/activities/<string:oid>", methods=["GET"])
def activity(oid):
	resultJson = convertDict(activityLog.objects.get(id = oid))
	return jsonify(resultJson)

@app.route("/api/activities/", methods=["GET"])
def activities():
	return jsonify(activityDatas[0:10])

@app.route("/api/activities/", methods=["POST"])
def activites_posting():
	
	if not request.json:
		abort(400)

	saveData = activityLogging(
		user_id=request.json["user_id"],
		username=request.json["username"],
		timestamp=datetime.datetime.utcnow,
		details=request.json["details"],
	)
	
	#save to database
	saveData.save()	

	#return 201 on success
	return jsonify(postData), 201
