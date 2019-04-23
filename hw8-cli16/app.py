import connexion

#Create the applicatoin instance
app = connexion.App(__name__, specification_dir='./')

#Create a URL route in our application for "/"
@app.route('/')
def home():
	return "hello world"


#Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')


# if we are running in stand alone mode, run the application
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
