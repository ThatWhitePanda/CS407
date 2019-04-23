import pytest
from flask import Flask, jsonify, abort, request, url_for
from app import app, activityLog
import json, requests

@pytest.fixture
def client():
	app.config["WTF_CSRF_ENABLED"] = False
	app.config["SERVER_NAME"] = "pytest-hw3"

	client = app.test_client()
	
	#drop the DB collection
	activityLog.drop_collection()
	
	#pushing the app context allows us to make calls to the app like url_for
	#as if we were running Flask app. Makes testing routes more resilient.
	ctx = app.app_context()
	ctx.push()

	#let pytest handle the stuff
	yield client
	ctx.pop()

#testing random index page
def test_get_plural_activities_returns_a_list_of_individual_activities(client):
	activityLog(user_id = 1, details="testing")
	testing = activityLog.objects(user_id = 1) 
	response = client.get(url_for('activities'))
	assert response.status_code == 200

def test_single_get(client):
	url = "https://activitylogger-cli16.herokuapp.com/api/activities/5c02d1bdec8ee8000b2784f3"
	r = requests.get(url)
	jsonData = json.loads(r.text)
	#assert {jsonData[0]['username']} == "john"

def test_get_all(client):
	url = "https://activitylogger-cli16.herokuapp.com/api/activities/"	
	r = requests.get(url)
	jsonData = json.loads(r.text)
	assert {jsonData[0]['user_id']} == {1}


