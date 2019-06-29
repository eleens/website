# _*_ coding:utf-8 _*_

"""
#=============================================================================
#  ProjectName: website
#     FileName: models
#         Desc: 
#       Author: yutingting
#        Email:
#     HomePage:
#       Create: 2019-04-28 22:53
#=============================================================================
"""
from mysite import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return "<User %r>" % self.username


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.ForeignKey(User.id), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           server_default=db.func.current_timestamp())
    author = db.relationship(User, lazy="joined", backref="posts")

