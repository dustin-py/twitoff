from flask import Flask
from .db_model import DB, User, Tweet


def create_app():
	"""Create and cnfigure an instance of the Flask app"""
	app = Flask(__name__)
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///twitoff.db'
	DB.init_app(app)

	@app.route("/")
	def root():
		return "Hello Twitoff"


	@app.route("/adduser/<username>/<followers>")
	def add_user(username, followers):
		user = User(username=username, followers=followers)
		DB.session.add(user)
		DB.session.commit()
		return f"{username} has been added to the DB."


	@app.route("/addtweet/<tweet>/<user_id>")
	def add_tweet(tweet, user_id): 
		string = Tweet(tweet=tweet, user_id=user_id)
		DB.session.add(string)
		DB.session.commit()
		return f"{tweet}\nhas been added to the DB."
	
	return app

#u1 = user(username='austen', followers=1500)
#DB.session.add(u1)
#DB.session.commit()
