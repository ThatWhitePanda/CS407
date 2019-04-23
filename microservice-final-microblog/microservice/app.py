from flask import Flask, jsonify

app = Flask(__name__)

posts = [
    {
     'id': 0,
     'title': "Intesting post",
     'content': 'Lorem ipsum etc.',
     'author': 'Poe',
    },
    {
     'id': 1,
     'title': "Storing data from csv file",
     'content': 'So I wanted a project that included a gui so I decided to write a',
     'author': 'Joe',
    },
    {
     'id': 2,
     'title': "Django Rest Framework serialisation",
     'content': "I'm new to Python/Django and having trouble trying..",
     'author': 'Moe',
    },
]

votes = [
    {
     'post_id': 0,
     'vote_count': -1,
    },
    {
     'post_id': 1,
     'vote_count': 5,
    },
    {
     'post_id': 2,
     'vote_count': 42,
    },
]


@app.route('/')
def testing_page():
	return "testing page"


@app.route('/api/vote_count/<int:id>', methods=["GET"])
def get_vote_count_by_id(id):
#	if (id > len(votes)):
#		abort(404)
	result = votes[id]
	return jsonify(result)



@app.route('/api/vote_count/', methods=["GET"])
def get_all_vote_count():
	result = votes
	return jsonify(result)
