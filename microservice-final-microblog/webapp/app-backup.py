from flask import Flask, abort, render_template, jsonify
import requests, json
#from microservice.app import get_all_vote_count, get_vote_count_by_id

app = Flask(__name__)

posts = [
    {
        'id': 0,
        'title': "Interesting post",
        'content': 'Lorem ipsum etc.',
        'author': 'Poe',
    },
    {
        'id': 1,
        'title': "Storing data from csv file",
        'content': 'So I wanted a project that included a gui so I decided to write a script that would help me calculate wind adjustments (and maybe other stuff down the line) for playing Golf Clash. Basically every club has an "accuracy" and is affected differently depending on wind strength. I created a spreadsheet containing all the attributes for each club and saved it as a csv file. Here is a small sample...',  # noqa: E501
        'author': 'Joe',
    },
    {
        'id': 2,
        'title': "Django Rest Framework serialisation",
        'content': "I'm new to Python/Django and having trouble trying to serialize a N-N relation using Django Rest Framework.",  # noqa: E501
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
def index():
	return render_template(
		"index.html",
		title="Microblog for Microservices",
		posts=posts,
		votes=votes,
	) 

@app.route('/post/<int:post_id>')
def post(post_id):
	r = requests.get('http://0.0.0.0:5001/api/vote_count/' + str(post_id))
	json_data = r.json()
	if post_id < 0 or post_id >= len(posts):
		abort(404)
	
	post = json_data['post_id']
	vote_count = json_data['vote_count']
	return render_template(
		"post.html",
		#title=str(post['title']),
		post=str(post),
		vote_count=str(vote_count),
	)	
