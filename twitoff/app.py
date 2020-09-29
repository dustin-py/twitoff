from flask import Flask

def create_app():
	"""Create and cnfigure an instance of the Flask app"""
	app = Flask(__name__)

	@app.route("/")
	def root():
		return "Hello Twitoff"

	return app
