from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class User(DB.Model):
    Id = DB.Column(DB.Integer, primary_key=True)
    username = DB.Column(DB.String(80), unique=True, nullable=False)
    followers = DB.Column(DB.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
    
# class Text(DB.Model):
#     Id = DB.Column(DB.Integer, primary_key=True)
#     text = DB.Column(DB.String(280), unique=True, nullable=False)
#     user_id = DB.Column(DB.ForeignKey('user.id'))
#     user = DB.relationship('user', backref=DB.backref('tweet', lazy=True))
    
    # def __repr__(self):
    #     return '<User %r>' % self.username