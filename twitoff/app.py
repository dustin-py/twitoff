from flask import Flask, render_template, request
from .db_model import DB, User, Tweet
from .twitter import add_user_tweepy

def create_app():
	"""Create and cnfigure an instance of the Flask app"""
	app = Flask(__name__)
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///twitoff.db'
	DB.init_app(app)

	@app.route("/")
	def root():
		return render_template('base.html',
                         		title='Home',
                           		users=User.query.all())


	@app.route('/user', methods=['POST'])
	@app.route('/user/<name>', methods=['GET'])
	def add_or_update_user(name=None, message=''):
		name = name or request.values['user_name']

		try:
			if request.method == "POST":
				add_user_tweepy(name)
				message = "User {} successfully added!".format(name)
			tweets = User.query.filter(User.username == name).one().tweet
		except Exception as e:
			print(f'Error adding {name}: {e}')
			tweets = []
			
		return render_template('user.html', title=name, tweets=tweets, message=message)
	# @app.route("/adduser/<username>/<followers>")
	# def add_user(username, followers):
	# 	user = User(username=username, followers=followers)
	# 	DB.session.add(user)
	# 	DB.session.commit()
	# 	return f"{username} has been added to the DB."


	# @app.route("/addtweet/<tweet>/<user_id>")
	# def add_tweet(tweet, user_id): 
	# 	string = Tweet(tweet=tweet, user_id=user_id)
	# 	DB.session.add(string)
	# 	DB.session.commit()
	# 	return f"{tweet}\nhas been added to the DB."
	
	return app

#u1 = user(username='austen', followers=1500)
#DB.session.add(u1)
#DB.session.commit()
