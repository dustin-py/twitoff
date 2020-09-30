from flask import Flask
from .db_model import DB

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///twitoff.db'
DB.init_app(app)

def create_app():
	"""Create and cnfigure an instance of the Flask app"""
	app = Flask(__name__)
	@app.route("/")
	def root():
		return "Hello Twitoff"

	return app
