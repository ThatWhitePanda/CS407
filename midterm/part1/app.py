from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
	return 'TESTING PAGE'


@app.route('/api/stringdata/<string:wordData>', methods=["GET"])
def stringdata(wordData):
	length = len(wordData) #get the length of the string
	reversedWord = wordData[::-1] #aka, [begin:end:step]
	upperWord = wordData.upper() #set the string to all uppercase
	
	#return the result
	return jsonify({"length:": length, "reversed:": reversedWord, "upper:": upperWord})
