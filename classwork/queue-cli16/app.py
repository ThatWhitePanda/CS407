from flask import Flask, jsonify
import time
import os
from celery import Celery


app = Flask(__name__)
app = Celery('tasks', broker='redis://localhost')

#get the environment sleep time variable
seconds_to_sleep = os.getenv('SLEEP_TIME')

@app.route('/')
def index():
	#sleep for 5 seconds before returning the page
	#convert the string environment variable to integer
	time.sleep(int(seconds_to_sleep))
	return 'TESTING PAGE'

@app.task
def add(x, y):
	return x + y
