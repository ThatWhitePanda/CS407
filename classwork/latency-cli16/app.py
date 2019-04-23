from flask import Flask, jsonify
import time
import os

app = Flask(__name__)

#get the environment sleep time variable
seconds_to_sleep = os.getenv('SLEEP_TIME')

@app.route('/')
def index():
	#sleep for 5 seconds before returning the page
	#convert the string environment variable to integer
	time.sleep(int(seconds_to_sleep))
	return 'TESTING PAGE'
